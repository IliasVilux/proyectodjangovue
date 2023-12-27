// Here goes the request of "colaborador" data using GraphQL

export async function load({ params }) {
	if (params.dni) {
		const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.dni}`);
		const colaborador_json = await response.json();

		return colaborador_json;
	}

    return null
}

export const actions = {
    create: () => {
    },
    update: () => {
    }
}