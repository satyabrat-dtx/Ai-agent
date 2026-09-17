# DB2ADMIN.PMWRKINSPECTIONREGISTRYRPT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84453

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `SERIALNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `INSPECTIONITEMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `INSPECTIONITEMCODE` | CHAR(15) |  |  |  |  |
| 5 | `INSPECTIONITEMLINENO` | INTEGER | NOT NULL |  |  |  |
| 6 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 8 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 9 | `DIVISIONCODE` | CHAR(8) |  |  |  | Division within a company; second-level organisational discriminator. |
| 10 | `MANNUALITEM` | CHAR(15) |  |  |  |  |
| 11 | `INSPECTIONDATE` | DATE |  |  |  |  |
| 12 | `INSPECTIONTIME` | TIMESTAMP |  |  |  |  |
| 13 | `STATUSTYPE` | INTEGER | NOT NULL |  |  |  |
| 14 | `READINGUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `INITIALREADING` | DECIMAL(15,5) |  |  |  |  |
| 16 | `CURRENTREADING` | DECIMAL(15,5) |  |  |  |  |
| 17 | `READINGDIFF` | DECIMAL(15,5) |  |  |  |  |
| 18 | `INSPECTIONBY` | CHAR(100) |  |  |  |  |
| 19 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMWRKINSPECTIONREGISTRYRPTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.SERIALNO,
       t.INSPECTIONITEMCOUNTERCODE,
       t.INSPECTIONITEMCODE,
       t.INSPECTIONITEMLINENO,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.DEPARTMENTCODE,
       t.DIVISIONCODE,
       t.MANNUALITEM,
       t.INSPECTIONDATE
FROM   DB2ADMIN.PMWRKINSPECTIONREGISTRYRPT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
