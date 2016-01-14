%global pkg_name maven-compiler-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        3.1
Release:        4.10%{?dist}
Summary:        Maven Compiler Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-compiler-plugin
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-plugin-plugin
BuildRequires:  %{?scl_prefix}maven-shared-incremental
BuildRequires:  %{?scl_prefix}maven-surefire-provider-junit
BuildRequires:  %{?scl_prefix}maven-doxia-sitetools
BuildRequires:  %{?scl_prefix}maven-plugin-testing-harness
BuildRequires:  %{?scl_prefix}maven-toolchain
BuildRequires:  %{?scl_prefix}plexus-compiler >= 2.0


%description
The Compiler Plugin is used to compile the sources of your project.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 3.1-4.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 3.1-4.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.5
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.1-4
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Apr 24 2013 Michal Srb <msrb@redhat.com> - 3.1-2
- Build against proper maven-shared-incremental artifactId

* Wed Apr 24 2013 Michal Srb <msrb@redhat.com> - 3.1-1
- Update to upstream version 3.1

* Tue Mar 05 2013 Michal Srb <msrb@redhat.com> - 3.0-2
- Build against proper plexus-compiler

* Tue Jan 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0-1
- Update to upstream version 3.0
- Build with xmvn
- Install license files, resolves: rhbz#895544

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5.1-1
- Updated to latest upstream version (2.5.1)

* Wed May 23 2012 Tomas Radej <tradej@redhat.com> - 2.4-1
- Updated to latest upstream version
- Guidelines fixes + Removed RPM workaround

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.2-4
- Add few missing (Build)requires
- Remove post(un) scriptlets with update_maven_depmap
- Use new add_maven_depmap macro

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.2-3
- Do not require maven2.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.2-1
- Update to latest version (2.3.2)
- Modifications according to new guidelines
- Build with maven 3

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.2-2
- Add missing requires.

* Tue May 11 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.2-1
- Initial package.
