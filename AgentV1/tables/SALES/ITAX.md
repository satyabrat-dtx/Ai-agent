# DB2ADMIN.ITAX

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `CODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 3 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122369

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TAXCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `TAXAPPLICATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `FORMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 9 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 10 | `CALCULATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 11 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 13 | `SIGN` | INTEGER | NOT NULL |  |  |  |
| 14 | `CALCULATIONBASISCODE` | CHAR(3) |  |  |  |  |
| 15 | `MODVATSETOFF` | INTEGER | NOT NULL |  |  |  |
| 16 | `MODVAT` | INTEGER | NOT NULL |  |  |  |
| 17 | `MODVATCYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 18 | `MODVATNYPERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 19 | `ALLOCATIONBASIS` | INTEGER | NOT NULL |  |  |  |
| 20 | `ROUNDOFFTYPE` | INTEGER | NOT NULL |  |  |  |
| 21 | `ROUNDOFFAMOUNT` | DECIMAL(10,5) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 30 | `HSNCODE` | CHAR(20) |  | FK | foreign_key |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITAX.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `ITAX.CURRENCYCODE = CURRENCY.CODE` |
| `FORMTYPE_FORMTYPE` | `COMPANYCODE`, `FORMTYPECODE` | [`FORMTYPE`](../SALES/FORMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITAX.COMPANYCODE = FORMTYPE.COMPANYCODE AND ITAX.FORMTYPECODE = FORMTYPE.CODE` |
| `TARIFF_HSN` | `HSNCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `ITAX.HSNCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ITAX_TAXCODE` | [`RTDDETAIL`](../SALES/RTDDETAIL.md) | `REPTAXDETREPORTTAXCOMPANYCODE`, `TAXCODECODE`, `TAXCODEEFFECTIVEFROMDATE` | `RTDDETAIL.REPTAXDETREPORTTAXCOMPANYCODE = ITAX.COMPANYCODE AND RTDDETAIL.TAXCODECODE = ITAX.CODE AND RTDDETAIL.TAXCODEEFFECTIVEFROMDATE = ITAX.EFFECTIVEFROMDATE` |
| `ITAX_ITAX` | [`DBKALLOWEDTAXDETAIL`](../SALES/DBKALLOWEDTAXDETAIL.md) | `DBKDEFAULTCOMPANYCODE`, `ITAXCODE`, `ITAXEFFECTIVEFROMDATE` | `DBKALLOWEDTAXDETAIL.DBKDEFAULTCOMPANYCODE = ITAX.COMPANYCODE AND DBKALLOWEDTAXDETAIL.ITAXCODE = ITAX.CODE AND DBKALLOWEDTAXDETAIL.ITAXEFFECTIVEFROMDATE = ITAX.EFFECTIVEFROMDATE` |
| `ITAX_ITAX` | [`DEPBALLOWEDTAXDETAIL`](../SALES/DEPBALLOWEDTAXDETAIL.md) | `DEPBDEFAULTCOMPANYCODE`, `ITAXCODE`, `ITAXEFFECTIVEFROMDATE` | `DEPBALLOWEDTAXDETAIL.DEPBDEFAULTCOMPANYCODE = ITAX.COMPANYCODE AND DEPBALLOWEDTAXDETAIL.ITAXCODE = ITAX.CODE AND DEPBALLOWEDTAXDETAIL.ITAXEFFECTIVEFROMDATE = ITAX.EFFECTIVEFROMDATE` |

## Indexes

- `ITAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TAXCATEGORYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TAXAPPLICATIONTYPE,
       t.FORMTYPECODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CALCULATIONTYPE,
       t.VALUE
FROM   DB2ADMIN.ITAX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
