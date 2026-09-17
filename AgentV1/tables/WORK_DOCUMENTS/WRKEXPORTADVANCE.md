# DB2ADMIN.WRKEXPORTADVANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177750

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `CODE` | CHAR(5) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `BANKGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 7 | `BANKREFNO` | CHAR(30) |  |  |  |  |
| 8 | `BANKREFDATE` | DATE |  |  |  |  |
| 9 | `ADVANCEAMOUNTUSD` | DECIMAL(18,5) |  |  |  |  |
| 10 | `UTILIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `AVERAGERATE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `CURRENTADJUSTMENT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `BALANCE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKEXPORTADVANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.CHOOSE,
       t.COMPANYCODE,
       t.CODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.BANKREFNO,
       t.BANKREFDATE,
       t.ADVANCEAMOUNTUSD,
       t.UTILIZEDVALUE,
       t.AVERAGERATE
FROM   DB2ADMIN.WRKEXPORTADVANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
