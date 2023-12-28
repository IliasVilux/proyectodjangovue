// import { request, gql } from 'graphql-request';

// export async function load({ params }) {
// 	if (params.dniCifcolaborador) {
// 		const query = gql`
// 			query colaborador($dniCifColaborador: String!) {
// 				colaborador(dniCifColaborador: $dniCifColaborador) {
// 					dniCifColaborador
// 					nombreColaborador
// 					apellidosColaborador
// 				}
// 			}
// 		`;

// 		const variables = { dniCifColaborador: params.dniCifColaborador };

// 		const colaborador = await request('http://127.0.0.1:8000/graphql/', query, variables).then(
// 			(data) => {
// 				return { colaborador: data.colaborador };
// 			}
// 		);

// 		return colaborador.colaborador;
// 	}
// 	return null;
// }

// export const actions = {
// 	create: () => {},
// 	update: () => {}
// };