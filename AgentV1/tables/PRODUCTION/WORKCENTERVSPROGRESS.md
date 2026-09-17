# DB2ADMIN.WORKCENTERVSPROGRESS

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `ANALYSISTYPECODE`, `WORKCENTERCODE`, `PROGRESSTEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126340

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISTYPECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PROGRESSTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `PROGRESSTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSISTYPE` | `COMPANYCODE`, `ANALYSISTYPECODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERVSPROGRESS.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND WORKCENTERVSPROGRESS.ANALYSISTYPECODE = ANALYSISTYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WORKCENTERVSPROGRESS.COMPANYCODE = COMPANY.CODE` |
| `PRODUCTIONPROGRESSTEMPLATE_PROGRESSTEMPLATE` | `PROGRESSTEMPLATECOMPANYCODE`, `PROGRESSTEMPLATECODE` | [`PRODUCTIONPROGRESSTEMPLATE`](../PRODUCTION/PRODUCTIONPROGRESSTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERVSPROGRESS.PROGRESSTEMPLATECOMPANYCODE = PRODUCTIONPROGRESSTEMPLATE.COMPANYCODE AND WORKCENTERVSPROGRESS.PROGRESSTEMPLATECODE = PRODUCTIONPROGRESSTEMPLATE.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERVSPROGRESS.COMPANYCODE = WORKCENTER.COMPANYCODE AND WORKCENTERVSPROGRESS.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKCENTERVSPROGRESSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISTYPECODE,
       t.WORKCENTERCODE,
       t.PROGRESSTEMPLATECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID,
       t.PROGRESSTEMPLATECOMPANYCODE
FROM   DB2ADMIN.WORKCENTERVSPROGRESS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
