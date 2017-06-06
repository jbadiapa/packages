# Generated from recursive-open-struct-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name recursive-open-struct

Name: rubygem-%{gem_name}
Version: 1.0.4
Release: 1%{?dist}
Summary: OpenStruct subclass that returns nested hash attributes as RecursiveOpenStructs
Group: Development/Languages
License: MIT
URL: http://github.com/aetherknight/recursive-open-struct
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(pry)
# BuildRequires: rubygem(rspec) >= 3.2
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
RecursiveOpenStruct is a subclass of OpenStruct. It differs from
OpenStruct in that it allows nested hashes to be treated in a recursive
fashion. For example:
ros = RecursiveOpenStruct.new({ :a => { :b => 'c' } })
ros.a.b # 'c'
Also, nested hashes can still be accessed as hashes:
ros.a_as_a_hash # { :b => 'c' }.


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
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_instdir}/recursive-open-struct.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/AUTHORS.txt
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Mon Jun 05 2017 Juan Badia Payno <jbadiapa@redhat.com> - 1.0.4-1
- Initial package
