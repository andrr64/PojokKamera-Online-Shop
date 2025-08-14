export const webRoute = {
    home: '/',
    login: '/auth/login',
    register: '/auth/register',
    merek: (id: number) => `/merek/${id}`,
    not_found: '/notfound'
}