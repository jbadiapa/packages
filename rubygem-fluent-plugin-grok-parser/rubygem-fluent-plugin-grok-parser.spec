# Generated from fluent-plugin-grok-parser-0.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-grok-parser

Name: rubygem-%{gem_name}
Version: 0.3.1
Release: 1%{?dist}
Summary: Fluentd plugin to support Logstash-inspired Grok format
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/kiyoto/fluent-plugin-grok-parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit) >= 3.1.5
BuildRequires: rubygem(rake)
BuildRequires: rubygem(minitest) >= 4.3.2
BuildRequires: rubygem(minitest) < 5.0.0 
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(thread_safe)
BuildRequires: fluentd
Requires: fluentd
Requires: rubygems
BuildArch: noarch

%description
Fluentd plugin to support Logstash-inspired Grok format for parsing logs.


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

LANG="en_US.UTF-8" ruby -I"lib:test" "test/test_grok_parser.rb" "test/test_grok_parser_in_tcp.rb" "test/test_multiline_grok_parser.rb" 

popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.gitmodules
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/fluent-plugin-grok-parser.gemspec
%{gem_libdir}
%{gem_instdir}/patterns
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test

%changelog
* Mon Jun 05 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.3.1-1
- Initial package
