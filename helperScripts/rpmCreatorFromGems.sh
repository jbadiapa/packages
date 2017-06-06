#!/bin/bash

RUBY='https://rubygems.org'
GEMURL="$RUBY/gems/"
LIST=gemList
DIR=donwload
SPECDIR=spec

CURRENTPATH=`pwd`

mkdir -p $DIR
mkdir -p $SPECDIR

cd $DIR
cat ../$LIST | xargs -i curl -O $GEMURL{} 

for HTML in `ls`;
do
	LINK=`grep Download ${HTML} | awk '{print $6}' | awk -F\" '{print $2}'`
        FULLLINK="$RUBY$LINK"
	curl -O $FULLLINK
done

for GEM in `ls *.gem`;
do
	gem2rpm $GEM > ${GEM}.spec
	sed -i -e 's/vagrant/Juan Badia Payno <jbadiapa@redhat.com>/g' \
	       -e 's/Summary: fluentd plugin/Summary: Fluentd Plugin/g'\
	       -e 's/\n\n%package/created from the gemspec\n\n\n%package/g' ${GEM}.spec
	NAME=`ls "${GEM}.spec" | sed -r -e 's/-[0-9]+\.[0-9]+\.[0-9]+\.gem\.spec//g'`
	mv ${GEM}.spec ${NAME}.spec
done

mv *.spec ../${SPECDIR}
rm -f *
cd $CURRENTPATH

for FILE in `ls ${SPECDIR}`;
do
	spectool -g -C ../SOURCES ${SPECDIR}/${FILE}
	rpmbuild -bb --define="_sourcedir ${PWD}/../SOURCES"     --define="_srcrpmdir ${PWD}/../SRPM"     --define="_rpmdir ${PWD}/../RPM" ${SPECDIR}/${FILE}
        rpmbuild -bs --define="_sourcedir ${PWD}/../SOURCES"     --define="_srcrpmdir ${PWD}/../SRPM"     --define="_rpmdir ${PWD}/../RPM" ${SPECDIR}/${FILE}
	mkdir -p tmp
	mv ${SPECDIR}/${FILE} tmp/rubygem-${FILE}
	mv ${PWD}/../SRPM/*.rpm tmp
	cd tmp 
	NAME="rubygem-${FILE::-5}"
	fedora-review -n $NAME
        cd .. 	
done
