# DB2ADMIN.SCDM_PROP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `PY_IDENTIFIER`, `PY_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186760

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PY_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `PY_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `PY_S_DESC` | VARCHAR(30) |  |  |  |  |
| 3 | `PY_L_DESC` | VARCHAR(30) |  |  |  |  |
| 4 | `PY_TYPE` | CHAR(1) |  |  |  |  |
| 5 | `PY_PROP_LEN` | SMALLINT |  |  |  |  |
| 6 | `PY_NUM_OF_DEC` | SMALLINT |  |  |  |  |
| 7 | `PY_CNG_PROP_VAL_CAUSE_RESCHED` | CHAR(1) |  |  |  |  |
| 8 | `PY_RP_CONN_LEV_MAIN` | CHAR(1) |  |  |  |  |
| 9 | `PY_RP_ADD_WC_PROC` | CHAR(1) |  |  |  |  |
| 10 | `PY_RO_CMPAT_CHK` | CHAR(1) |  |  |  |  |
| 11 | `PY_RO_CONN_LEV_MAIN` | CHAR(1) |  |  |  |  |
| 12 | `PY_RO__ADD_WC_PROC` | CHAR(1) |  |  |  |  |
| 13 | `PY_RO_PROD_TYP` | CHAR(1) |  |  |  |  |
| 14 | `PY_OO_CMPAT_CHK` | CHAR(1) |  |  |  |  |
| 15 | `PY_OO_CONN_LEV_MAIN` | CHAR(1) |  |  |  |  |
| 16 | `PY_OO_ADD_WC_PROC` | CHAR(1) |  |  |  |  |
| 17 | `PY_OO_PROD_TYP` | CHAR(1) |  |  |  |  |
| 18 | `PY_MQMRELEVANCE` | CHAR(1) |  |  |  |  |
| 19 | `PY_MCMRELEVANCE` | CHAR(1) |  |  |  |  |
| 20 | `PY_PROP_INSTANCE_COUNTER` | VARCHAR(5) |  |  |  |  |
| 21 | `PY_PROPVAL_INSTANCE_COUNTER` | VARCHAR(90) |  |  |  |  |
| 22 | `PY_PROP_IS_DATE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.PY_IDENTIFIER,
       t.PY_PROPERTY,
       t.PY_S_DESC,
       t.PY_L_DESC,
       t.PY_TYPE,
       t.PY_PROP_LEN,
       t.PY_NUM_OF_DEC,
       t.PY_CNG_PROP_VAL_CAUSE_RESCHED,
       t.PY_RP_CONN_LEV_MAIN,
       t.PY_RP_ADD_WC_PROC,
       t.PY_RO_CMPAT_CHK,
       t.PY_RO_CONN_LEV_MAIN
FROM   DB2ADMIN.SCDM_PROP t
FETCH FIRST 100 ROWS ONLY;
```
