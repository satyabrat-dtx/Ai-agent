# DB2ADMIN.APPPRODUCTSTREE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 50
- **Primary key**: `COMPANYCODE`, `AGENTCODE`, `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110870

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `AGENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 4 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 5 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `STATISTICALGROUPCODE` | CHAR(6) |  | FK | foreign_key |  |
| 7 | `COLLECTIONCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `COLLECTIONCODE` | CHAR(6) |  | FK | foreign_key |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `FIRSTBREAKDOWNKEYIMAGELINK` | VARCHAR(250) |  |  |  |  |
| 22 | `FIRSTBREAKDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 23 | `SECONDBREAKDOWNKEYIMAGELINK` | VARCHAR(250) |  |  |  |  |
| 24 | `SECONDBREAKDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 25 | `THIRDBREAKDOWNKEYIMAGELINK` | VARCHAR(250) |  |  |  |  |
| 26 | `THIRDBREAKDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 27 | `FOURTHBREAKDOWNKEYIMAGELINK` | VARCHAR(250) |  |  |  |  |
| 28 | `FOURTHBREAKDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 29 | `FULLITEMKEYDESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 30 | `BASEUNITOFMEASURE` | CHAR(3) |  |  |  |  |
| 31 | `AVAILABLEQUANTITYINBASEUOM` | DECIMAL(15,5) |  |  |  |  |
| 32 | `USERUNITOFMEASURE` | CHAR(3) |  |  |  |  |
| 33 | `AVAILABLEQUANTITYINUSERUOM` | DECIMAL(15,5) |  |  |  |  |
| 34 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 35 | `UPTOQUANTITY1` | DECIMAL(15,5) |  |  |  |  |
| 36 | `PRICE1` | DECIMAL(18,5) |  |  |  |  |
| 37 | `UPTOQUANTITY2` | DECIMAL(15,5) |  |  |  |  |
| 38 | `PRICE2` | DECIMAL(18,5) |  |  |  |  |
| 39 | `UPTOQUANTITY3` | DECIMAL(15,5) |  |  |  |  |
| 40 | `PRICE3` | DECIMAL(18,5) |  |  |  |  |
| 41 | `UPTOQUANTITY4` | DECIMAL(15,5) |  |  |  |  |
| 42 | `PRICE4` | DECIMAL(18,5) |  |  |  |  |
| 43 | `UPTOQUANTITY5` | DECIMAL(15,5) |  |  |  |  |
| 44 | `PRICE5` | DECIMAL(18,5) |  |  |  |  |
| 45 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 46 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 47 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 48 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AGENT_AGENT` | `COMPANYCODE`, `AGENTCODE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPPRODUCTSTREE.COMPANYCODE = AGENT.COMPANYCODE AND APPPRODUCTSTREE.AGENTCODE = AGENT.CODE` |
| `COLLECTIONGROUP_COLLECTION` | `COLLECTIONCOMPANYCODE`, `COLLECTIONCODE` | [`COLLECTIONGROUP`](../CORE_MASTER/COLLECTIONGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPPRODUCTSTREE.COLLECTIONCOMPANYCODE = COLLECTIONGROUP.COMPANYCODE AND APPPRODUCTSTREE.COLLECTIONCODE = COLLECTIONGROUP.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `APPPRODUCTSTREE.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `APPPRODUCTSTREE.CURRENCYCODE = CURRENCY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPPRODUCTSTREE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND APPPRODUCTSTREE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `ORDERPARTNER_ORDERPARTNER` | `COMPANYCODE`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `APPPRODUCTSTREE.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND APPPRODUCTSTREE.ORDPRNCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND APPPRODUCTSTREE.ORDPRNCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `STATISTICALGROUP_STATISTICALGROUP` | `STATISTICALGROUPCOMPANYCODE`, `STATISTICALGROUPCODE` | [`STATISTICALGROUP`](../CORE_MASTER/STATISTICALGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPPRODUCTSTREE.STATISTICALGROUPCOMPANYCODE = STATISTICALGROUP.COMPANYCODE AND APPPRODUCTSTREE.STATISTICALGROUPCODE = STATISTICALGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPPRODUCTSTREEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.AGENTCODE,
       t.UNIQUEID,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.STATISTICALGROUPCOMPANYCODE,
       t.STATISTICALGROUPCODE,
       t.COLLECTIONCOMPANYCODE,
       t.COLLECTIONCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01
FROM   DB2ADMIN.APPPRODUCTSTREE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
