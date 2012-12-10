%define name		glc
%define release		1.2
%define version         0.5.8
%define develname %mklibname -d glc
%define libname %mklibname glc

Name:			%{name}
Version:		%{version}
Release:		%{release}
Summary:		ALSA and OpenGL video capture tool
License:		MIT
Group:			Video
URL:			https://github.com/nullkey/glc
Source0:		https://nodeload.github.com/nullkey/glc/tarball/master/glc-0.5.8.tar.bz2
ExclusiveArch:		i586 x86_64
BuildRequires:		cmake 
BuildRequires:		pkgconfig(libpng)
BuildRequires:		pkgconfig(xorg-server)
BuildRequires:		gcc 
BuildRequires:		gcc-c++ 
BuildRequires:		make 
BuildRequires:		libelfhacks-devel
BuildRequires:		libpacketstream-devel
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(glu)
BuildRequires:		pkgconfig(ao)
BuildRequires:		pkgconfig(xxf86vm)
BuildRequires:		pkgconfig(alsa)
BuildRequires:      png-devel
Requires:               %{libname}  = %{version}-%{release}

%description	
glc is an ALSA and OpenGL video capture tool that you 
can use to record the output from opengl applications.

%prep  
%setup -q -n %{name}-%{version}

%build 
export CC="/usr/bin/gcc -pthread"
cmake -D CMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix} -DLIB_INSTALL_DIR=%{buildroot}%{_libdir} .
%make 

%install 
%makeinstall
%ifarch x86_64
install -d   %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/libglc* %{buildroot}%{_libdir}/
%endif


%files -n %{name}
%defattr(0755,root,root)
%{_bindir}/glc*

#------------------
%package -n %{libname}
Summary:   Shared library for %{name}
Group:     System/Libraries
Requires:  %{name}

%description -n %{libname}
This project provides a client library for %{name}

%files -n %{libname}
%defattr(0755,root,root)
%{_libdir}/libglc*

#-----------------
%package -n %{develname}
Summary: Development files for %{name}
Provides: %{name}-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{develname}
%defattr(0755,root,root)
%{_includedir}/*


