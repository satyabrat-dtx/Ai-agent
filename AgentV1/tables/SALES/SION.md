# DB2ADMIN.SION

- **Module**: `SALES` (low confidence — FK neighbourhood: 2 of 2 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123491

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `STEP` | CHAR(1) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `ITEMDESCRIPTION` | VARCHAR(370) |  |  |  |  |
| 19 | `ITEMTECHCHARACTERISTICS` | VARCHAR(200) |  |  |  |  |
| 20 | `ITCCODE` | CHAR(20) |  | FK | foreign_key |  |
| 21 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 27 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 28 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SION.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SION.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND SION.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `TARIFF_ITC` | `ITCCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `SION.ITCCODE = TARIFF.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SION.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SION_LINE` | [`SIONDETAIL`](../INTERNAL_ORDERS/SIONDETAIL.md) | `SIONCOMPANYCODE`, `SIONCODE` | `SIONDETAIL.SIONCOMPANYCODE = SION.COMPANYCODE AND SIONDETAIL.SIONCODE = SION.CODE` |
| `SION_SION` | [`ADVSION`](../SALES/ADVSION.md) | `ADVANCELICENSECOMPANYCODE`, `SIONCODE` | `ADVSION.ADVANCELICENSECOMPANYCODE = SION.COMPANYCODE AND ADVSION.SIONCODE = SION.CODE` |
| `SION_SION` | [`PSINVLINE`](../SALES/PSINVLINE.md) | `PSINVOICECOMPANYCODE`, `SIONCODE` | `PSINVLINE.PSINVOICECOMPANYCODE = SION.COMPANYCODE AND PSINVLINE.SIONCODE = SION.CODE` |
| `SION_SION` | [`PRECOMMINVOICELINE`](../CORE_MASTER/PRECOMMINVOICELINE.md) | `PRECOMMINVOICECOMPANYCODE`, `SIONCODE` | `PRECOMMINVOICELINE.PRECOMMINVOICECOMPANYCODE = SION.COMPANYCODE AND PRECOMMINVOICELINE.SIONCODE = SION.CODE` |

## Indexes

- `SIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.STEP,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.SION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
