# Generated from unf-0.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unf

Name: rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Summary: A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
Group: Development/Languages
License: BSD
URL: https://github.com/knu/ruby-unf
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(shoulda)
BuildArch: noarch

%description
This is a wrapper library to bring Unicode Normalization Form support
to Ruby/JRuby.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

sed -i -e 's/\/usr\/bin\/env rake/\/bin\/rake/g' %{gem_name}-%{version}/Rakefile

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

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/unf.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Mon Jun 05 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.1.4-1
- Initial package
