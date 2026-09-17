# DB2ADMIN.EXTOPDOCUMENTLINEIE

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `EXTOPDOCUMENTCOMPANYCODE`, `EXTOPDOCUMENTPROVCOUNTERCODE`, `EXTOPDOCUMENTPROVISIONALCODE`, `ORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181959

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPDOCUMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPDOCPROVCNTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `EXTOPDOCUMENTPROVCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `EXTOPDOCUMENTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 6 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_EXTOPDOCUMENTCOMPANY` | `EXTOPDOCUMENTCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXTOPDOCUMENTLINEIE.EXTOPDOCUMENTCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPDOCUMENTLINEIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPDOCUMENTCOMPANYCODE,
       t.EXTOPDOCPROVCNTCOMPANYCODE,
       t.EXTOPDOCUMENTPROVCOUNTERCODE,
       t.EXTOPDOCUMENTPROVISIONALCODE,
       t.ORDERLINE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.BASICVALUE,
       t.GROSSVALUE,
       t.NETTVALUE,
       t.ROUNDOFFVALUE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EXTOPDOCUMENTLINEIE t
FETCH FIRST 100 ROWS ONLY;
```
