# DB2ADMIN.SCDA_BALANCE_DETAIL

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `BD_IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184572

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `BD_TYPE_PROD` | VARCHAR(3) | NOT NULL |  |  |  |
| 2 | `BD_PRODUCT_CODE` | VARCHAR(120) | NOT NULL |  |  |  |
| 3 | `BD_NET_GROUP_CODE` | VARCHAR(16) | NOT NULL |  |  |  |
| 4 | `BD_DUE_DATE` | TIMESTAMP | NOT NULL |  |  |  |
| 5 | `BD_OCCUPY_CODE` | VARCHAR(20) | NOT NULL |  |  |  |
| 6 | `BD_INFO_AREA` | VARCHAR(90) |  |  |  |  |
| 7 | `BD_QTY` | DECIMAL(11,2) |  |  |  |  |
| 8 | `BD_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 9 | `BD_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.BD_IDENTIFIER,
       t.BD_TYPE_PROD,
       t.BD_PRODUCT_CODE,
       t.BD_NET_GROUP_CODE,
       t.BD_DUE_DATE,
       t.BD_OCCUPY_CODE,
       t.BD_INFO_AREA,
       t.BD_QTY,
       t.BD_USR_NAMECG,
       t.BD_USR_TIMECG
FROM   DB2ADMIN.SCDA_BALANCE_DETAIL t
FETCH FIRST 100 ROWS ONLY;
```
