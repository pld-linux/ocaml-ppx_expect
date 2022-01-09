#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Cram like framework for OCaml
Summary(pl.UTF-8):	Szkielet w stylu Cram dla OCamla
Name:		ocaml-ppx_expect
Version:	0.14.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_expect/tags
Source0:	https://github.com/janestreet/ppx_expect/archive/v%{version}/ppx_expect-%{version}.tar.gz
# Source0-md5:	ce1bb859cf695eb8f165fe1e03fff2c1
URL:		https://github.com/janestreet/ppx_expect
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_here-devel >= 0.14
BuildRequires:	ocaml-ppx_here-devel < 0.15
BuildRequires:	ocaml-ppx_inline_test-devel >= 0.14
BuildRequires:	ocaml-ppx_inline_test-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
BuildRequires:	ocaml-re-devel >= 1.8.0
BuildRequires:	ocaml-stdio-devel >= 0.14
BuildRequires:	ocaml-stdio-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Generation of fast comparison and equality functions from type
expressions and definitions.

This package contains files needed to run bytecode executables using
ppx_expect library.

%description -l pl.UTF-8
Generowanie szybkich funkcji porównujących i przyrównujących z wyrażeń
i definicji typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_expect.

%package devel
Summary:	Cram like framework for OCaml - development part
Summary(pl.UTF-8):	Szkielet w stylu Cram dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_here-devel >= 0.14
Requires:	ocaml-ppx_inline_test-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.18.0
Requires:	ocaml-re-devel >= 1.8.0
Requires:	ocaml-stdio-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_expect library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_expect.

%prep
%setup -q -n ppx_expect-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_expect/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_expect/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_expect

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.org
%dir %{_libdir}/ocaml/ppx_expect
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/ppx.exe
%{_libdir}/ocaml/ppx_expect/META
%{_libdir}/ocaml/ppx_expect/*.cma
%dir %{_libdir}/ocaml/ppx_expect/collector
%{_libdir}/ocaml/ppx_expect/collector/runtime.js
%{_libdir}/ocaml/ppx_expect/collector/*.cma
%dir %{_libdir}/ocaml/ppx_expect/common
%{_libdir}/ocaml/ppx_expect/common/*.cma
%dir %{_libdir}/ocaml/ppx_expect/config
%{_libdir}/ocaml/ppx_expect/config/*.cma
%dir %{_libdir}/ocaml/ppx_expect/config_types
%{_libdir}/ocaml/ppx_expect/config_types/*.cma
%dir %{_libdir}/ocaml/ppx_expect/evaluator
%{_libdir}/ocaml/ppx_expect/evaluator/*.cma
%dir %{_libdir}/ocaml/ppx_expect/matcher
%{_libdir}/ocaml/ppx_expect/matcher/*.cma
%dir %{_libdir}/ocaml/ppx_expect/payload
%{_libdir}/ocaml/ppx_expect/payload/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/collector/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/common/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/config/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/config_types/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/evaluator/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/matcher/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_expect/payload/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllexpect_test_collector_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_expect/*.cmi
%{_libdir}/ocaml/ppx_expect/*.cmt
%{_libdir}/ocaml/ppx_expect/*.cmti
%{_libdir}/ocaml/ppx_expect/*.mli
%{_libdir}/ocaml/ppx_expect/collector/libexpect_test_collector_stubs.a
%{_libdir}/ocaml/ppx_expect/collector/*.cmi
%{_libdir}/ocaml/ppx_expect/collector/*.cmt
%{_libdir}/ocaml/ppx_expect/collector/*.cmti
%{_libdir}/ocaml/ppx_expect/collector/*.mli
%{_libdir}/ocaml/ppx_expect/common/*.cmi
%{_libdir}/ocaml/ppx_expect/common/*.cmt
%{_libdir}/ocaml/ppx_expect/common/*.cmti
%{_libdir}/ocaml/ppx_expect/common/*.mli
%{_libdir}/ocaml/ppx_expect/config/*.cmi
%{_libdir}/ocaml/ppx_expect/config/*.cmt
%{_libdir}/ocaml/ppx_expect/config/*.cmti
%{_libdir}/ocaml/ppx_expect/config/*.mli
%{_libdir}/ocaml/ppx_expect/config_types/*.cmi
%{_libdir}/ocaml/ppx_expect/config_types/*.cmt
%{_libdir}/ocaml/ppx_expect/config_types/*.cmti
%{_libdir}/ocaml/ppx_expect/config_types/*.mli
%{_libdir}/ocaml/ppx_expect/evaluator/*.cmi
%{_libdir}/ocaml/ppx_expect/evaluator/*.cmt
%{_libdir}/ocaml/ppx_expect/evaluator/*.cmti
%{_libdir}/ocaml/ppx_expect/evaluator/*.mli
%{_libdir}/ocaml/ppx_expect/matcher/*.cmi
%{_libdir}/ocaml/ppx_expect/matcher/*.cmt
%{_libdir}/ocaml/ppx_expect/matcher/*.cmti
%{_libdir}/ocaml/ppx_expect/matcher/*.mli
%{_libdir}/ocaml/ppx_expect/payload/*.cmi
%{_libdir}/ocaml/ppx_expect/payload/*.cmt
%{_libdir}/ocaml/ppx_expect/payload/*.cmti
%{_libdir}/ocaml/ppx_expect/payload/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_expect/ppx_expect.a
%{_libdir}/ocaml/ppx_expect/*.cmx
%{_libdir}/ocaml/ppx_expect/*.cmxa
%{_libdir}/ocaml/ppx_expect/collector/expect_test_collector.a
%{_libdir}/ocaml/ppx_expect/collector/*.cmx
%{_libdir}/ocaml/ppx_expect/collector/*.cmxa
%{_libdir}/ocaml/ppx_expect/common/expect_test_common.a
%{_libdir}/ocaml/ppx_expect/common/*.cmx
%{_libdir}/ocaml/ppx_expect/common/*.cmxa
%{_libdir}/ocaml/ppx_expect/config/expect_test_config.a
%{_libdir}/ocaml/ppx_expect/config/*.cmx
%{_libdir}/ocaml/ppx_expect/config/*.cmxa
%{_libdir}/ocaml/ppx_expect/config_types/expect_test_config_types.a
%{_libdir}/ocaml/ppx_expect/config_types/*.cmx
%{_libdir}/ocaml/ppx_expect/config_types/*.cmxa
%{_libdir}/ocaml/ppx_expect/evaluator/ppx_expect_evaluator.a
%{_libdir}/ocaml/ppx_expect/evaluator/*.cmx
%{_libdir}/ocaml/ppx_expect/evaluator/*.cmxa
%{_libdir}/ocaml/ppx_expect/matcher/expect_test_matcher.a
%{_libdir}/ocaml/ppx_expect/matcher/*.cmx
%{_libdir}/ocaml/ppx_expect/matcher/*.cmxa
%{_libdir}/ocaml/ppx_expect/payload/ppx_expect_payload.a
%{_libdir}/ocaml/ppx_expect/payload/*.cmx
%{_libdir}/ocaml/ppx_expect/payload/*.cmxa
%endif
%{_libdir}/ocaml/ppx_expect/dune-package
%{_libdir}/ocaml/ppx_expect/opam
%{_examplesdir}/%{name}-%{version}
