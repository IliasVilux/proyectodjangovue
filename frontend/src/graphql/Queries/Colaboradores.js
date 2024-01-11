import { gql } from "@apollo/client/core";

const COLABORADOR_FRAGMENT = gql`
  fragment ColaboradorFragment on ColaboradorType {
    dniCifColaborador
    nombreColaborador
  }
`;

export const GET_COLABORADORES = gql`
	query allColaboradores {
		colaboradores {
			...ColaboradorFragment
		}
	}
	${COLABORADOR_FRAGMENT}
`;

export const GET_COLABORADOR = gql`
	query colaborador($dniCifColaborador: String!) {
		colaborador(dniCifColaborador: $dniCifColaborador) {
			...ColaboradorFragment
		}
	}
	${COLABORADOR_FRAGMENT}
`;