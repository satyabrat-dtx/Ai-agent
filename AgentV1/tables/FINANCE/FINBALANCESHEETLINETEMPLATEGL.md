# DB2ADMIN.FINBALANCESHEETLINETEMPLATEGL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `FINBALANCESHEETTEMPLATECODE`, `FINBLNSHEETLINETEMPLATECODE`, `GLCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 174168

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FINBLNSTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `FINBALANCESHEETTEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINBLNSHEETLINETEMPLATECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `GLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `GLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `BALANCETYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `NEGATIVEMULTIPLIER` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINBALANCESHEETLINETEMPLATEGL.COMPANYCODE = COMPANY.CODE` |
| `FINBALANCESHEETTEMPLATE_FINBALANCESHEETTEMPLATE` | `FINBLNSTEMPLATECOMPANYCODE`, `FINBALANCESHEETTEMPLATECODE` | [`FINBALANCESHEETTEMPLATE`](../FINANCE/FINBALANCESHEETTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINBALANCESHEETLINETEMPLATEGL.FINBLNSTEMPLATECOMPANYCODE = FINBALANCESHEETTEMPLATE.COMPANYCODE AND FINBALANCESHEETLINETEMPLATEGL.FINBALANCESHEETTEMPLATECODE = FINBALANCESHEETTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINBLNSHEETLINETEMPLATEGLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FINBLNSTEMPLATECOMPANYCODE,
       t.FINBALANCESHEETTEMPLATECODE,
       t.FINBLNSHEETLINETEMPLATECODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.BALANCETYPE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.FINBALANCESHEETLINETEMPLATEGL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
