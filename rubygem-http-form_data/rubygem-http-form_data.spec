# Generated from http-form_data-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name http-form_data

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 1%{?dist}
Summary: http-form_data-1.0.3
Group: Development/Languages
License: MIT
URL: https://github.com/httprb/form_data.rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9
BuildArch: noarch

%description
Utility-belt to build form data request bodies. Provides support for
`application/x-www-form-urlencoded` and `multipart/form-data` types.


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




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%{gem_instdir}/CHANGES.md
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/appveyor.yml
%exclude %{gem_instdir}/http-form_data.gemspec
%exclude %{gem_instdir}/spec/fixtures/expected-multipart-body.tpl
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/spec/fixtures/expected-multipart-body.tpl
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 1.0.3-1
- Initial package
