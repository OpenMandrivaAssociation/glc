%define name		glc
Name:			%{name}
Version:		0.5.8
%define rel		1
Release:		%mkrel %rel
Summary:		ALSA and OpenGL video capture tool
License:		MIT
Group:			Video
URL:			https://github.com/nullkey/glc
BuildRoot:		%_tmppath/%{name}-%{version}-%{release}-buildroot
Source0:		glc-0.5.8.tar.bz2
ExclusiveArch:		i586 x86_64
BuildRequires:		cmake png-devel x11-server-devel
BuildRequires:		gcc gcc-c++ make libelfhacks libpacketstream mesagl-devel mesaglu-devel
BuildRequires:		libao-devel libxxf86vm-devel libalsa-devel

%description	
glc is an ALSA and OpenGL video capture tool that you 
can use to record the output from opengl applications.

%prep  
%setup -q -n %{name}-%{version}

%build 
cmake -D CMAKE_INSTALL_PREFIX=%{buildroot}/%{_prefix} .
%make

%install 
rm -rf $RPM_BUILD_ROOT
%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}
%defattr(0755,root,root)
%{_libdir}/libglc*
%{_includedir}/*
%{_bindir}/glc*

