import { gql } from "@apollo/client/core";

export const GET_COLABORADORES = gql`
	query allColaboradores {
		colaboradores {
			dniCifColaborador
			nombreColaborador
		}
	}
`;

export const GET_COLABORADOR = gql`
	query colaborador($dniCifColaborador: String!) {
		colaborador(dniCifColaborador: $dniCifColaborador) {
			dniCifColaborador
			nombreColaborador
		}
	}
`;