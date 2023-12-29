<script>
	import {
		gql,
		Client,
		cacheExchange,
		fetchExchange,
		setContextClient,
		getContextClient,
		queryStore,
		mutationStore
	} from '@urql/svelte';
	import ColaboradorCard from '../../components/ColaboradorCard.svelte';

	const client = new Client({
		url: 'http://localhost:8000/graphql/',
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

	function deleteColaboradorMutation(dniCifColaborador) {
		mutationStore({
			client: client,
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
			variables: { dniCifColaborador: dniCifColaborador }
		});
	}

	const deleteClick = (dniCifColaborador) => {
		deleteColaboradorMutation(dniCifColaborador);
	};
</script>

<div class="container">
	<h1>colaboradores</h1>

	<a href="colaboradores/añadir" class="btn">Agregar Nuevo Colaborador</a>

	{#if $colaboradores.fetching}
		<p>Loading...</p>
	{:else if $colaboradores.error}
		<p>Oh no... {$colaboradores.error.message}</p>
	{:else}
		<ul style="padding: 0; margin-top: 2rem;">
			{#each $colaboradores.data.colaboradores as colaborador (colaborador.dniCifColaborador)}
				<ColaboradorCard
					dni={colaborador.dniCifColaborador}
					on:clicked={deleteClick(colaborador.dniCifColaborador)}
				/>
			{/each}
		</ul>
	{/if}
</div>

<style>
	.container {
		width: 45%;
		margin: auto;
	}
	.btn {
		background-color: #020d19;
		color: #e0e0e0;
		padding: 10px;
		border-radius: 10px;
	}
	h1{
		text-align: center;
		text-transform: uppercase;
		margin-bottom: 4rem;
	}
</style>
