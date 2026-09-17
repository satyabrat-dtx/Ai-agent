# DB2ADMIN.FINDOCMAXAMTALLOWED

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `USERUSERID`, `TEMPLATECODE`, `FROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 174689

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 6 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 7 | `MAXAMTALLOWED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USER` | `USERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `FINDOCMAXAMTALLOWED.USERUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINDOCMAXAMTALLOWED.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINDOCMAXAMTALLOWED.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINDOCMAXAMTALLOWED.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `FINDOCUMENTTEMPLATE_TEMPLATE` | `TEMPLATECOMPANYCODE`, `TEMPLATECODE` | [`FINDOCUMENTTEMPLATE`](../FINANCE/FINDOCUMENTTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINDOCMAXAMTALLOWED.TEMPLATECOMPANYCODE = FINDOCUMENTTEMPLATE.COMPANYCODE AND FINDOCMAXAMTALLOWED.TEMPLATECODE = FINDOCUMENTTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINDOCMAXAMTALLOWEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.USERUSERID,
       t.TEMPLATECOMPANYCODE,
       t.TEMPLATECODE,
       t.FROMDATE,
       t.TODATE,
       t.MAXAMTALLOWED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINDOCMAXAMTALLOWED t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
