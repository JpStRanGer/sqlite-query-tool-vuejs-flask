// Create a new Vue app
const app = Vue.createApp({
    // Set custom delimiters for Vue templates
    delimiters: ["[[", "]]"],

    // Set initial data values
    data() {
        return {
            DB_select: "*", // Default SQL SELECT statement
            DB_table: ["tags", "alt2", "alt3"], // List of tables to query from
            DB_views: ["tags", "alt2", "alt3"], // List of views to query from
            columns: ["test"], // Placeholder values for columns and rows
            rows: ["data"], // Placeholder values for columns and rows
            selectedTable: "", // Selected table to query
            results: false, // Boolean to track if results are displayed
            helpfullQuerys: [
                {
                    title: "Get name of all tables",
                    query: "SELECT name FROM sqlite_master WHERE type='table'",
                },
                {
                    title: "Get name of all views",
                    query: "SELECT name FROM sqlite_master WHERE type='view' or type='table'"
                },
            ],
        };
    },
    watch: {},
    // Call getTableData() when the app is created
    created() {
        this.getTableData();
        this.getViewData();
    },

    // Define app methods
    methods: {
        // Get a list of tables and views from the SQLite database
        async getTableData() {
            try {
                // Make a POST request to the server to retrieve table/view names
                const response = await fetch("/query", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        query: "SELECT name FROM sqlite_master WHERE type='table'",
                    }),
                });

                // Extract the response JSON data
                const data = await response.json();

                // Flatten the data array and convert each item to a string
                this.DB_table = data.rows.flat().map((item) => item.toString());
                // this.DB_table = data.rows.flat();
            } catch (error) {
                // Log any errors that occur
                console.log(
                    "There was an error -",
                    error,
                    " in getTableData()."
                );
            }
        },
        // Get a list of tables and views from the SQLite database
        async getViewData() {
            try {
                // Make a POST request to the server to retrieve table/view names
                const response = await fetch("/query", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        query: "SELECT name FROM sqlite_master WHERE type='view'",
                    }),
                });

                // Extract the response JSON data
                const data = await response.json();

                // Flatten the data array and convert each item to a string
                this.DB_views = data.rows.flat().map((item) => item.toString());
                // this.DB_table = data.rows.flat();
            } catch (error) {
                // Log any errors that occur
                console.log(
                    "There was an error -",
                    error,
                    " in getViewData()."
                );
            }
        },

        // Run a test SQL query
        async postQuery() {
            console.log("running:postQuery()");

            // Construct the full SQL query string
            const DB_query =
                "SELECT " + this.DB_select + " FROM " + this.selectedTable;

            try {
                // Make a POST request to the server to execute the SQL query
                const response = await fetch("/query", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ query: DB_query }),
                });

                // Extract the response JSON data
                const data = await response.json();

                console.log(data);

                // Update the app's data values with the query results
                this.testVar = data.columns;
                this.columns = data.columns;
                this.rows = data.rows;
                this.results = true;
            } catch (error) {
                // Log any errors that occur
                console.log("There was an error -", error, " in postQuery.");
            }
        },
    },
});

// Mount the Vue app to the specified HTML element
app.mount("#app");
