# `kb.sqlite` reference

Read-only index over the same content as `catalog/` and `graph/`. Use it when you
want set-based lookups instead of loading JSON.

```
tables(name, module, module_confidence, module_basis, roles, queryable, notes,
       primary_key, n_columns, n_inbound_fk, n_outbound_fk, ddl_line)
columns(table_name, name, position, sql_type, nullable, col_default,
        in_primary_key, is_foreign_key, tags, meaning)
primary_keys(table_name, ordinal, column_name)
foreign_keys(id, constraint_name, child, parent, child_columns, parent_columns,
             on_delete, on_update, enforced, on_clause)
fk_columns(fk_id, ordinal, child_column, parent_column)
indexes_(name, table_name, columns, is_unique)
join_edges(a, b, fk_id, direction, cardinality, on_clause)   -- both directions
implicit_links(child_table, child_column, parent_table, parent_column,
               confidence, basis, on_clause)
modules(key, description, n_tables, label_reliability)
views(name, depends_on, sql)
routines(kind, name, ddl_line)
meta(key, value)                                             -- JSON values
tables_fts(name, module, roles, notes, column_names)         -- FTS5
columns_fts(column_name, table_name)                         -- FTS5
```

`queryable = 0` marks staging mirrors and BPM-engine internals. Filter them out
of any candidate-table search.

## Recipes

```sql
-- candidate tables for a question
SELECT name, module FROM tables_fts
 JOIN tables USING (name)
WHERE tables_fts MATCH 'delivery AND warehouse' AND queryable = 1
LIMIT 20;

-- which tables hold a given column
SELECT table_name, in_primary_key FROM columns WHERE name = 'CUSTOMERSUPPLIERCODE';

-- the full key of a table, in order
SELECT column_name FROM primary_keys WHERE table_name = 'SALESORDER' ORDER BY ordinal;

-- everything joinable to a table in one hop, with the predicate
SELECT b, direction, cardinality, on_clause FROM join_edges WHERE a = 'SALESORDER';

-- children that fan out (aggregate these)
SELECT b, on_clause FROM join_edges WHERE a = 'SALESORDER' AND cardinality = 'one_to_many';

-- tables to avoid as join waypoints
SELECT name, n_inbound_fk FROM tables ORDER BY n_inbound_fk DESC LIMIT 20;

-- unresolved implicit parents
SELECT child_table FROM implicit_links WHERE parent_table IS NULL;
```
