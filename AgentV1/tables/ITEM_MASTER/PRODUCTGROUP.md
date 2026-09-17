# DB2ADMIN.PRODUCTGROUP

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `SCHEMETYPECODE`, `PRODUCTGROUPCODE`, `DEPBSRNO`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123131

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SCHEMETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PRODUCTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `DEPBSRNO` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 6 | `DEPBRATE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 7 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `CUTPERCENTAGE` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 11 | `CUTAPPLICABLEAFTER` | INTEGER | NOT NULL |  |  |  |
| 12 | `CUT2PERCENTAGE` | DECIMAL(9,5) |  |  |  |  |
| 13 | `CUT2APPLICABLEAFTER` | INTEGER | NOT NULL |  |  |  |
| 14 | `PRODUCTDESCRIPTION` | VARCHAR(250) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTGROUP.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTGROUP.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PRODUCTGROUP.CURRENCYCODE = CURRENCY.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTGROUP.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND PRODUCTGROUP.SCHEMETYPECODE = SCHEMETYPE.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PRODUCTGROUP.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRODUCTGROUP_PRODUCTGROUP` | [`EXPORTSHIPPINGLINE`](../ITEM_MASTER/EXPORTSHIPPINGLINE.md) | `PRODUCTGROUPCOMPANYCODE`, `PRODUCTGROUPSCHEMETYPECODE`, `PRODUCTGROUPPRODUCTGROUPCODE`, `PRODUCTGROUPDEPBSRNO`, `PRODUCTGROUPEFFECTIVEFROMDATE` | `EXPORTSHIPPINGLINE.PRODUCTGROUPCOMPANYCODE = PRODUCTGROUP.COMPANYCODE AND EXPORTSHIPPINGLINE.PRODUCTGROUPSCHEMETYPECODE = PRODUCTGROUP.SCHEMETYPECODE AND EXPORTSHIPPINGLINE.PRODUCTGROUPPRODUCTGROUPCODE = PRODUCTGROUP.PRODUCTGROUPCODE AND EXPORTSHIPPINGLINE.PRODUCTGROUPDEPBSRNO = PRODUCTGROUP.DEPBSRNO AND EXPORTSHIPPINGLINE.PRODUCTGROUPEFFECTIVEFROMDATE = PRODUCTGROUP.EFFECTIVEFROMDATE` |

## Indexes

- `PRODUCTGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SCHEMETYPECODE,
       t.PRODUCTGROUPCODE,
       t.DEPBSRNO,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.DEPBRATE,
       t.UNITOFMEASURECODE,
       t.CURRENCYCODE,
       t.VALUE,
       t.CUTPERCENTAGE,
       t.CUTAPPLICABLEAFTER
FROM   DB2ADMIN.PRODUCTGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
