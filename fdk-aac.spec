Name:      fdk-aac
Version:   0.1.4
#Ne pas enlever le .ives a la fin de la release !
#Cela est utilise par les scripts de recherche de package.
Release:   1.ives_distrib
Summary:   AAC codec library
Vendor:    Fraunhofer Institute
Group:     Library/Multimedia
License:   AAC Patent Licensing 
URL:       http://sourceforge.net/projects/opencore-amr/files/fdk-aac
BuildArchitectures: ives_archi
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: 

%description
The Fraunhofer FDK AAC Codec Library for Android is a low resource implementation of AAC encoders and decoders available for Android on ARM, MIPS, and x86 processors

%package devel
Summary: Libraries, includes to develop applications with %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the header files and static libraries for
building apps and func which use %{name}.
  
%clean
echo "############################# Clean"
echo Clean du repertoire $RPM_BUILD_ROOT
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%prep
./autogen.sh
./configure --prefix=/usr --libdir=%{_libdir} --shlibdir=%{_libdir} --enable-shared --disable-ffplay --disable-ffserver --enable-pic
make

%install
echo "Install" $PWD
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.so.*
/usr/bin/*
%{_libdir}/pkgconfig/
/usr/share/ffmpeg/*.ffpreset
/usr/share/doc/lame/
/usr/share/man/man1/
/usr/share/ffmpeg/ffprobe.xsd

%files devel
%defattr(-,root,root)
%attr(0755,root,root) /usr/include/*/*.h
%{_libdir}/*.a
/usr/share/ffmpeg/examples/

%changelog
* Mon Mar 17 2015 Emmanuel BUU <emmanuel.buu@ives.fr>
- integration ffmpeg 2.2.14
