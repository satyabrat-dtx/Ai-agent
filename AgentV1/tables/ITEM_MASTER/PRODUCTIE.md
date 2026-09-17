# DB2ADMIN.PRODUCTIE

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'PRODUCT')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124746

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `TARIFFCODE` | CHAR(20) |  | FK | foreign_key |  |
| 15 | `TAXTEMPLATEDETAILTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 16 | `TAXTEMPLATEDETAILCODE` | CHAR(3) |  |  |  |  |
| 17 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 18 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 19 | `GSTWITHINSTATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 20 | `GSTWITHINSTATECODE` | CHAR(3) |  |  |  |  |
| 21 | `GSTINTERSTATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 22 | `GSTINTERSTATECODE` | CHAR(3) |  |  |  |  |
| 23 | `SHIPMENTARTICLECODE` | CHAR(5) |  | FK | foreign_key |  |
| 24 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `SHIPMENTARTICLECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIE.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PRODUCTIE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `SHIPMENTARTICLE_SHIPMENTARTICLE` | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | [`SHIPMENTARTICLE`](../OTHER/SHIPMENTARTICLE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIE.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND PRODUCTIE.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `PRODUCTIE.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.PRODUCTIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
