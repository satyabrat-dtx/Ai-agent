# DB2ADMIN.WRKREPLENISHMENTREQCREATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24972

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ORDERLINKTYPE` | CHAR(2) |  |  |  |  |
| 5 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REPLENISHMENTREQCREATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ORDERLINKTYPE,
       t.ORDERCOUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.ORDERCOMPONENTLINE,
       t.ORDERDELIVERYLINE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKREPLENISHMENTREQCREATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
