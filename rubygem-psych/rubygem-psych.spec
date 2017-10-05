# Generated from psych-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name psych

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Summary: Psych is a YAML parser and emitter
Group: Development/Languages
License: MIT ???? 
URL: http://github.com/tenderlove/psych
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 1.9.2
# BuildRequires: rubygem(rake-compiler) >= 0.4.1
# BuildRequires: rubygem(hoe) >= 3.6
# BuildRequires: rubygem(hoe) < 4

%description
Psych is a YAML parser and emitter.  Psych leverages
libyaml[http://pyyaml.org/wiki/LibYAML]
for its YAML parsing and emitting capabilities.  In addition to wrapping
libyaml, Psych also knows how to serialize and de-serialize most Ruby objects
to and from the YAML format.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/*.so %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_instdir}/.autotest
%exclude %{gem_instdir}/.gemtest
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/Manifest.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Wed Sep 27 2017 vagrant - 2.0.0-1
- Initial package
