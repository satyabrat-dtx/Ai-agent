# DB2ADMIN.SALESORDERTEMPLATEIE

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130012

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 3 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 4 | `DEFAULTTAXFROM` | INTEGER | NOT NULL |  |  |  |
| 5 | `RELEASEMFLAG` | INTEGER | NOT NULL |  |  |  |
| 6 | `INVOICEMFLAG` | INTEGER | NOT NULL |  |  |  |
| 7 | `TAXTEMPLATEAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 8 | `LCNOTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `BENIFITNOTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `TYPEOFINVOICE` | INTEGER | NOT NULL |  |  |  |
| 11 | `INTERCOMPANYTAXCOPY` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESORDERTEMPLATEIE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERTEMPLATEIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.TAXTEMPLATEHEADERTEMPLATETYPE,
       t.TAXTEMPLATEHEADERCODE,
       t.DEFAULTTAXFROM,
       t.RELEASEMFLAG,
       t.INVOICEMFLAG,
       t.TAXTEMPLATEAPPLICABLE,
       t.LCNOTREQUIRED,
       t.BENIFITNOTREQUIRED,
       t.TYPEOFINVOICE,
       t.INTERCOMPANYTAXCOPY
FROM   DB2ADMIN.SALESORDERTEMPLATEIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
