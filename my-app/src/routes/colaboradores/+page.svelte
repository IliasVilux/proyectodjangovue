<script>
	import ColaboradorCard from '../../components/ColaboradorCard.svelte';
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

	$: colaboradores = queryStore({
		client: getContextClient(),
		query: gql`
			query colaboradores {
				colaboradores {
					dniCifColaborador
					nombreColaborador
				}
			}
		`
	});

	const deleteColaborador = (dni) => {
		result = mutationStore({
			client: getContextClient(),
			query: gql`
				mutation deleteColaborador($dniCifColaborador: String!) {
					deleteColaborador(dniCifColaborador: $dniCifColaborador) {
						colaborador {
							dniCifColaborador
							nombreColaborador
						}
					}
				}
			`,
			variables: { dniCifColaborador: dni }
		});
	};
</script>

<div class="container">
	<h1>colaboradores</h1>

	<a href="colaboradores/formulario" class="btn">Agregar Nuevo Colaborador</a>

	{#if $colaboradores.fetching}
		<p>Loading...</p>
	{:else if $colaboradores.error}
		<p>Oh no... {$colaboradores.error.message}</p>
	{:else}
		<ul>
			{#each $colaboradores.data.colaboradores as colaborador}
				<ColaboradorCard
					dni={colaborador.dniCifColaborador}
					on:clicked={deleteColaborador(colaborador.dniCifColaborador)}
				/>
			{/each}
		</ul>
	{/if}
</div>

<style>
	.container {
		width: 45%;
		margin: auto;
		text-align: center;
	}
	.btn {
		margin-left: auto;
		background-color: #020d19;
		color: #e0e0e0;
		text-decoration: none;
		padding: 10px;
		border-radius: 10px;
	}
</style>
