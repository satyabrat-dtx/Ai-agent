# DB2ADMIN.MILAUTHUSERCUSTOMER

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `USERUSERID`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`, `AREACODE`, `COUNTRYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33380

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `USERUSERID` | CHAR(25) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `AREACODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `COUNTRYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 10 | `AREACOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USER` | `USERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `MILAUTHUSERCUSTOMER.USERUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MILAUTHUSERCUSTOMER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MILAUTHUSERCUSTOMERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.USERUSERID,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.AREACODE,
       t.COUNTRYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.AREACOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.MILAUTHUSERCUSTOMER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
