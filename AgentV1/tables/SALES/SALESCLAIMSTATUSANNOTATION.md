# DB2ADMIN.SALESCLAIMSTATUSANNOTATION

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93071

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) |  | FK | foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 4 | `CLAIMPROGRESSSTATUSCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `PLANNERANNOTATION` | VARCHAR(250) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CLAIMSTATUSDEFINITION_CLAIMPROGRESSSTATUS` | `COMPANYCODE`, `CLAIMPROGRESSSTATUSCODE` | [`CLAIMSTATUSDEFINITION`](../SALES/CLAIMSTATUSDEFINITION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESCLAIMSTATUSANNOTATION.COMPANYCODE = CLAIMSTATUSDEFINITION.COMPANYCODE AND SALESCLAIMSTATUSANNOTATION.CLAIMPROGRESSSTATUSCODE = CLAIMSTATUSDEFINITION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESCLAIMSTATUSANNOTATION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESCLAIMSTATUSANNOTATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANYCODE,
       t.CODE,
       t.LINE,
       t.CLAIMPROGRESSSTATUSCODE,
       t.PLANNERANNOTATION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.SALESCLAIMSTATUSANNOTATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
