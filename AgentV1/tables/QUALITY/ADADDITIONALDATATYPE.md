# DB2ADMIN.ADADDITIONALDATATYPE

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `NAME`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8527

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 2 | `LENGTH` | INTEGER | NOT NULL |  |  |  |
| 3 | `DECIMALS` | INTEGER | NOT NULL |  |  |  |
| 4 | `JAVATYPENAME` | CHAR(50) | NOT NULL |  |  |  |
| 5 | `HTMLTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `HTMLROWS` | INTEGER | NOT NULL |  |  |  |
| 7 | `MINLENGTH` | INTEGER | NOT NULL |  |  |  |
| 8 | `HTMLSIZE` | INTEGER | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ADADDITIONALDATATYPE_TYPE` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `TYPENAME` | `ADADDITIONALDATA.TYPENAME = ADADDITIONALDATATYPE.NAME` |
| `ADADDITIONALDATATYPE_ENTRYCODE` | [`QATEST`](../QUALITY/QATEST.md) | `ENTRYCODENAME` | `QATEST.ENTRYCODENAME = ADADDITIONALDATATYPE.NAME` |
| `ADADDITIONALDATATYPE_FRMCDATATYPE` | [`QATEST`](../QUALITY/QATEST.md) | `FRMCDATATYPENAME` | `QATEST.FRMCDATATYPENAME = ADADDITIONALDATATYPE.NAME` |

## Indexes

- `ADADDITIONALDATATYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NAME,
       t.DESCRIPTION,
       t.LENGTH,
       t.DECIMALS,
       t.JAVATYPENAME,
       t.HTMLTYPE,
       t.HTMLROWS,
       t.MINLENGTH,
       t.HTMLSIZE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADADDITIONALDATATYPE t
FETCH FIRST 100 ROWS ONLY;
```
