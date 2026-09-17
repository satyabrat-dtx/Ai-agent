# DB2ADMIN.SCDA_PROP

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `PY_IDENTIFIER`, `PY_PROPERTY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183880

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
| 8 | `PY_PROP_VAL_TAKE_FOR_MERGE` | CHAR(1) |  |  |  |  |
| 9 | `PY_RP_CONN_LEV_MAIN` | CHAR(1) |  |  |  |  |
| 10 | `PY_RP_ADD_WC_PROC` | CHAR(1) |  |  |  |  |
| 11 | `PY_RO_CMPAT_CHK` | CHAR(1) |  |  |  |  |
| 12 | `PY_RO_CONN_LEV_MAIN` | CHAR(1) |  |  |  |  |
| 13 | `PY_RO__ADD_WC_PROC` | CHAR(1) |  |  |  |  |
| 14 | `PY_RO_PROD_TYP` | CHAR(1) |  |  |  |  |
| 15 | `PY_OO_CMPAT_CHK` | CHAR(1) |  |  |  |  |
| 16 | `PY_OO_CONN_LEV_MAIN` | CHAR(1) |  |  |  |  |
| 17 | `PY_OO_ADD_WC_PROC` | CHAR(1) |  |  |  |  |
| 18 | `PY_OO_PROD_TYP` | CHAR(1) |  |  |  |  |
| 19 | `PY_MQMRELEVANCE` | CHAR(1) |  |  |  |  |
| 20 | `PY_MCMRELEVANCE` | CHAR(1) |  |  |  |  |
| 21 | `PY_DESIGNATEDPROPERTY` | VARCHAR(2) |  |  |  |  |
| 22 | `PY_IS_PROP_BUILD_FROM_PROP` | CHAR(1) |  |  |  |  |
| 23 | `PY_PROP_VAL_BUILDED1` | VARCHAR(5) |  |  |  |  |
| 24 | `PY_PROP_VAL_BUILDED2` | VARCHAR(5) |  |  |  |  |
| 25 | `PY_PROP_VAL_BUILDED3` | VARCHAR(5) |  |  |  |  |
| 26 | `PY_PROP_VAL_BUILDED4` | VARCHAR(5) |  |  |  |  |
| 27 | `PY_PROP_VAL_BUILDED5` | VARCHAR(5) |  |  |  |  |
| 28 | `PY_PROP_INSTANCE_COUNTER` | VARCHAR(5) |  |  |  |  |
| 29 | `PY_PROPVAL_INSTANCE_COUNTER` | VARCHAR(90) |  |  |  |  |
| 30 | `PY_PROP_IS_DATE` | CHAR(1) |  |  |  |  |

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
       t.PY_PROP_VAL_TAKE_FOR_MERGE,
       t.PY_RP_CONN_LEV_MAIN,
       t.PY_RP_ADD_WC_PROC,
       t.PY_RO_CMPAT_CHK
FROM   DB2ADMIN.SCDA_PROP t
FETCH FIRST 100 ROWS ONLY;
```
