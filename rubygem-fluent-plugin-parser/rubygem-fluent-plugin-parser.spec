# Generated from fluent-plugin-parser-0.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-parser

Name: rubygem-%{gem_name}
Version: 0.6.1
Release: 1%{?dist}
Summary: Fluentd plugin to parse/combine log messages
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/tagomoris/fluent-plugin-parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(oj)
BuildRequires: rubygem(rake)
Requires: fluentd
BuildArch: noarch

%description
fluentd plugin to parse single field, or to combine log structure into single
field.


%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

sed -i -e 's/\/usr\/bin\/env rake/\/bin\/rake/g' %{gem_name}-%{version}/Rakefile
chmod 744 %{gem_name}-%{version}/Rakefile 

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}
rake test
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/fluent-plugin-parser.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Sun Jun 04 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.6.1-1
- Initial package
