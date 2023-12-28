<script>
	import {
		Client,
		cacheExchange,
		fetchExchange,
		setContextClient,
		queryStore,
		mutationStore,
		gql,
		getContextClient
	} from '@urql/svelte';

	const client = new Client({
		url: 'http://127.0.0.1:8000/graphql/',
		exchanges: [cacheExchange, fetchExchange]
	});
	setContextClient(client);

	export let data;

    let colaborador = queryStore({
		client: getContextClient(),
		query: gql`
			query colaboradores($dniCifColaborador: String!) {
				colaborador(dniCifColaborador: $dniCifColaborador) {
					dniCifColaborador
					nombreColaborador
				}
			}
		`,
		variables: { dniCifColaborador: data.dniCifColaborador }
	});

	async function handleSubmit() {
		console.log($colaborador.data.colaborador);
	}
</script>

{#if $colaborador.fetching}
	<p>Loading...</p>
{:else if $colaborador.error}
	<p>Oh no... <b>{$colaborador.error.message}</b></p>
{:else}
	<form method="POST" on:submit|preventDefault={handleSubmit}>
		<input type="text" name="dni" bind:value={$colaborador.data.colaborador.dniCifColaborador} />
		<input
			type="text"
			name="name"
			value={$colaborador.data.colaborador.nombreColaborador
				? $colaborador.data.colaborador.nombreColaborador
				: ''}
		/>

		{#if !data.dniCifColaborador}
			<button type="submit" disabled={$colaborador.data.colaborador.dniCifColaborador.length < 1}
				>Crear</button
			>
		{:else}
			<button type="submit">Modificar</button>
		{/if}
	</form>
{/if}
