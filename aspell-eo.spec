%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE: as of version 0.50-2, the wordlist isn't using accents;
# so we fix that with a small script in %setup section; that should
# be removed once an accented wordlist is included

%define src_ver 2.1.20000225a-2
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal esperanto
%define languageeng esperanto
%define languageenglazy Esperanto
%define languagecode eo
%define lc_ctype eo_XX

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       2.1.20000225a.2
Release:       %mkrel 5
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:	       http://aspell.sourceforge.net/
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-eo


BuildRequires: aspell
Requires:      aspell

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary

# RedHat Stuff. is this right:
#Obsoletes: ispell-eo, ispell-esperanto

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
./configure
#%make

# the word list doesn't use accents; fixing that
cat << EOF > fixaccents.sh
#!/bin/bash
cat - | \
  sed 's/C[Xx]/ĉ/g' | sed 's/cx/ĉ/g' | \
  sed 's/G[Xx]/Ĝ/g' | sed 's/gx/ĝ/g' | \
  sed 's/H[Xx]/Ĥ/g' | sed 's/hx/ĥ/g' | \
  sed 's/J[Xx]/Ĵ/g' | sed 's/jx/ĵ/g' | \
  sed 's/S[Xx]/Ŝ/g' | sed 's/sx/ŝ/g' | \
  sed 's/U[Xx]/Ŭ/g' | sed 's/ux/ŭ/g' | \
  iconv -f utf-8 -t iso-8859-3
EOF
preunzip -c eo.cwl | sh ./fixaccents.sh | (LC_ALL=C sort) > eo.wl
aspell  --lang=eo create master ./eo.rws < eo.wl

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# fix doc perms
chmod 644 README

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.20000225a.2-4mdv2011.0
+ Revision: 662808
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.20000225a.2-3mdv2011.0
+ Revision: 603203
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.20000225a.2-2mdv2010.1
+ Revision: 518917
- rebuild

* Fri Jun 26 2009 Isabel Vallejo <isabel@mandriva.org> 2.1.20000225a.2-1mdv2010.0
+ Revision: 389573
- update to 2.1.20000225a-2
- update to 2.1.20000225a-2

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.2-10mdv2009.1
+ Revision: 350015
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-9mdv2009.0
+ Revision: 220372
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.2-8mdv2008.1
+ Revision: 182416
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-7mdv2008.1
+ Revision: 148751
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-6mdv2007.1
+ Revision: 145022
- Import aspell-eo

* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-6mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-5mdk
- enabled real esperanto (with accents)

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.2-4mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-3mdk
- allow build on ia64

