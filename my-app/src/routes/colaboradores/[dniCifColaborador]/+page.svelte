<script>
	import {
		Client,
		cacheExchange,
		fetchExchange,
		setContextClient,
		queryStore,
		gql,
		mutationStore
	} from '@urql/svelte';
	import { goto } from '$app/navigation';

	const client = new Client({
		url: 'http://localhost:8000/graphql/',
		exchanges: [cacheExchange, fetchExchange]
	});
	setContextClient(client);

	export let data;
	let dataGetted = false;
	$: form = {
		dniCifColaborador: '',
		nombreColaborador: ''
	};

	let colaborador = queryStore({
		client: client,
		query: gql`
			query colaborador($dniCifColaborador: String!) {
				colaborador(dniCifColaborador: $dniCifColaborador) {
					dniCifColaborador
					nombreColaborador
				}
			}
		`,
		variables: { dniCifColaborador: data.dniCifColaborador }
	});

	$: if ($colaborador.data && $colaborador.data.colaborador && !dataGetted) {
		form.dniCifColaborador = $colaborador.data.colaborador.dniCifColaborador;
		form.nombreColaborador = $colaborador.data.colaborador.nombreColaborador;
		dataGetted = true;
	}

	function handleSubmit() {
		if (data.dniCifColaborador === 'añadir') {
			mutationStore({
				client: client,
				query: gql`
					mutation addColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
						addColaborador(
							dniCifColaborador: $dniCifColaborador
							nombreColaborador: $nombreColaborador
						) {
							colaborador {
								dniCifColaborador
								nombreColaborador
							}
						}
					}
				`,
				variables: {
					dniCifColaborador: form.dniCifColaborador,
					nombreColaborador: form.nombreColaborador
				}
			});
		} else {
			mutationStore({
				client: client,
				query: gql`
					mutation updateColaborador($dniCifColaborador: String!, $nombreColaborador: String!) {
						updateColaborador(
							dniCifColaborador: $dniCifColaborador
							nombreColaborador: $nombreColaborador
						) {
							colaborador {
								dniCifColaborador
								nombreColaborador
							}
						}
					}
				`,
				variables: {
					dniCifColaborador: form.dniCifColaborador,
					nombreColaborador: form.nombreColaborador
				}
			});
		}
		goto('/colaboradores')
	}
</script>

<form on:submit|preventDefault={handleSubmit}>
	<input type="text" name="dni" bind:value={form.dniCifColaborador} />
	<input type="text" name="name" bind:value={form.nombreColaborador} />
	<button type="submit" disabled={form.dniCifColaborador.length < 1}>
		{data.dniCifColaborador === 'añadir' ? 'Crear' : 'Modificar'}
	</button>
</form>
