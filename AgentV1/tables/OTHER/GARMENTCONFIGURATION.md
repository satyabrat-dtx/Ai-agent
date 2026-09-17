# DB2ADMIN.GARMENTCONFIGURATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126929

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COLORSUBCODE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SIZESUBCODE` | INTEGER | NOT NULL |  |  |  |
| 6 | `PRODUCTTYPE` | CHAR(1) |  |  |  |  |
| 7 | `TYPE` | CHAR(1) |  |  |  |  |
| 8 | `USABLEINBUNDLE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `LOTFROMPR` | SMALLINT | NOT NULL |  |  |  |
| 10 | `LOTASPLANTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SPLITLINEINRECEIPT` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LEASTSALEABLEQUANTITY` | DECIMAL(5,2) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `GARMENTCONFIGURATION.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCONFIGURATION.COMPANYCODE = DIVISION.COMPANYCODE AND GARMENTCONFIGURATION.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `GARMENTCONFIGURATION.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND GARMENTCONFIGURATION.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `GARMENTCONFIGURATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.COLORSUBCODE,
       t.SIZESUBCODE,
       t.PRODUCTTYPE,
       t.TYPE,
       t.USABLEINBUNDLE,
       t.LOTFROMPR,
       t.LOTASPLANTINVOICE,
       t.SPLITLINEINRECEIPT
FROM   DB2ADMIN.GARMENTCONFIGURATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
