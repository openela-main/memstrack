# vim: syntax=spec

Name:           memstrack
Version:        0.2.4
Release:        2%{?dist}
Summary:        A memory allocation tracer, like a hot spot analyzer for memory allocation
License:        GPLv3
URL:            https://github.com/ryncsn/memstrack
VCS:            git+git@github.com:ryncsn/memstrack.git
BuildRequires:  gcc
BuildRequires:  ncurses-devel

Source:         https://github.com/ryncsn/memstrack/archive/refs/tags/v%{version}.tar.gz

Patch1: 0001-Skip-memcg-info-in-__process_stacktrace-for-page_own.patch
Patch2: 0002-Fix-data-type-error-in-perf_handle_mm_page_alloc.patch

%description
A memory allocation tracer, like a hot spot analyzer for memory allocation

%prep
%setup -q -n memstrack-%{version}
%patch1 -p1
%patch2 -p1

%build
%{set_build_flags}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 memstrack %{buildroot}/%{_bindir}

%files
%doc README.md
%license LICENSE
%{_bindir}/memstrack

%changelog
* Fri Jul 15 2022 Tao Liu <ltao@redhat.com> - 0.2.4-2
- Revert bz2107730

* Fri Jul 15 2022 Tao Liu <ltao@redhat.com> - 0.2.4-1
- Rebase to latest upstream(813c2feaa2f)

* Tue Aug 6 2020 Kairui Song <kasong@redhat.com> - 0.1.11-1
- Fix memstrack failure with large memory hole

* Tue Jul 14 2020 Kairui Song <kasong@redhat.com> - 0.1.8-2
- Fix TUI not quiting issue

* Sun Jun 28 2020 Kairui Song <kasong@redhat.com> - 0.1.8-1
- Bump to latest upstream version, fix some issues and introduce unit test

* Wed Jun 24 2020 Kairui Song <kasong@redhat.com> - 0.1.7-1
- Bump to latest upstream version to fix multiple bugs

* Wed May 20 2020 Kairui Song <kasong@redhat.com> - 0.1.4-1
- Bump to latest upstream version to fix some other issue found in early testing

* Tue May 19 2020 Kairui Song <kasong@redhat.com> - 0.1.3-1
- Bump to latest upstream version to fix problems found by rpmdiff

* Thu May 07 2020 Kairui Song <kasong@redhat.com> - 0.1.2-1
- Initial Release
