%bcond_with tests

Name:           docker-compose
Version:        1.14.0
Release:        1%{?dist}
Summary:        Multi-container orchestration for Docker
License:        ASL 2.0
URL:            https://github.com/docker/compose
Source0:        https://files.pythonhosted.org/packages/source/d/docker-compose/docker-compose-%{version}.tar.gz
Patch0:         remove-colorama-requirement.patch
Patch1:         remove-environment-markers.patch
Patch2:         relax-requirements.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if %{with tests}
BuildRequires:  pytest
BuildRequires:  python-mock >= 1.0.1
BuildRequires:  python-cached_property >= 1.2.0
BuildRequires:  python-docopt >= 0.6.1
BuildRequires:  PyYAML >= 3.10
BuildRequires:  python-requests >= 2.6.0
BuildRequires:  python-texttable >= 0.8.1
BuildRequires:  python-websocket-client >= 0.32.0
BuildRequires:  python-docker >= 2.3.0
BuildRequires:  python-dockerpty >= 0.4.1
BuildRequires:  python-six >= 1.3.0
BuildRequires:  python-jsonschema >= 2.5.1
BuildRequires:  python-enum34 >= 1.0.4
BuildRequires:  python-backports-ssl_match_hostname >= 3.5
BuildRequires:  python-ipaddress >= 1.0.16
%endif

Requires:       python-setuptools
Requires:       python-cached_property >= 1.2.0
Requires:       python-docopt >= 0.6.1
Requires:       PyYAML >= 3.10
Requires:       python-requests >= 2.6.0
Requires:       python-texttable >= 0.8.1
Requires:       python-websocket-client >= 0.32.0
Requires:       python-docker >= 2.3.0
Requires:       python-dockerpty >= 0.4.1
Requires:       python-six >= 1.3.0
Requires:       python-jsonschema >= 2.5.1
Requires:       python-enum34 >= 1.0.4
Requires:       python-backports-ssl_match_hostname >= 3.5
Requires:       python-ipaddress >= 1.0.16


%description
Compose is a tool for defining and running multi-container Docker
applications. With Compose, you use a Compose file to configure your
application's services. Then, using a single command, you create and
start all the services from your configuration.

Compose is great for development, testing, and staging environments,
as well as CI workflows.

Using Compose is basically a three-step process.

1. Define your app's environment with a Dockerfile so it can be
   reproduced anywhere.
2. Define the services that make up your app in docker-compose.yml so
   they can be run together in an isolated environment:
3. Lastly, run docker-compose up and Compose will start and run your
   entire app.


%prep
%autosetup -p 1


%build
%py2_build


%install
%py2_install


%if %{with tests}
%check
%{__python2} -m pytest -v tests/unit/
%endif


%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{_bindir}/docker-compose
%{python2_sitelib}/*


%changelog
* Wed Jul 26 2017 Carl George <carl@george.computer> - 1.14.0-1
- Initial package
