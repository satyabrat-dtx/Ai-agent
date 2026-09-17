# DB2ADMIN.PLANNINGTRACE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CREATIONID`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 35088

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL |  | audit |  |
| 5 | `PLANNINGBY` | CHAR(1) |  |  |  |  |
| 6 | `RUNDESCRIPTION` | CHAR(150) |  |  |  |  |
| 7 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 8 | `PROJECTCODE` | CHAR(20) |  | FK | foreign_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `MULTILINKSPLANNING` | SMALLINT | NOT NULL |  |  |  |
| 11 | `RESERVATIONPLANNING` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PLANNINGTRACE.COMPANYCODE = COMPANY.CODE` |
| `PROJECT_PROJECT` | `COMPANYCODE`, `PROJECTCODE` | [`PROJECT`](../CORE_MASTER/PROJECT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLANNINGTRACE.COMPANYCODE = PROJECT.COMPANYCODE AND PLANNINGTRACE.PROJECTCODE = PROJECT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANNINGTRACEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONID,
       t.LINE,
       t.CREATIONUSER,
       t.CREATIONTIMESTAMP,
       t.PLANNINGBY,
       t.RUNDESCRIPTION,
       t.SUBMITTEDJOBJOBNUMBER,
       t.PROJECTCODE,
       t.ABSUNIQUEID,
       t.MULTILINKSPLANNING,
       t.RESERVATIONPLANNING
FROM   DB2ADMIN.PLANNINGTRACE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
