// Here goes the request of "colaboradores" data using GraphQL
// import { request, gql } from 'graphql-request';

// export async function load() {
// 	const query = gql`
// 		query {
// 			colaboradores {
// 				dniCifColaborador
// 				nombreColaborador
// 			}
// 		}
// 	`;

// 	const colaboradores = await request('http://127.0.0.1:8000/graphql/', query).then((data) => {
// 		return { colaboradores: data.colaboradores };
// 	});

// 	return colaboradores;
// }

// import { Client, cacheExchange, fetchExchange, setContextClient } from '@urql/svelte';
// const client = new Client({
// 	url: 'http://127.0.0.1:8000/graphql/',
// 	exchanges: [cacheExchange, fetchExchange]
// });
// setContextClient(client);
