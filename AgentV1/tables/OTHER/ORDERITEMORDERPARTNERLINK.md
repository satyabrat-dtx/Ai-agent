# DB2ADMIN.ORDERITEMORDERPARTNERLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `EXTERNALITEMCODE`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2180

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 15 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 16 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 17 | `EXTERNALITEMCODE` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 18 | `EXTERNALDRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 19 | `EXTERNALREFERENCE` | CHAR(30) |  |  |  |  |
| 20 | `LEADTIMEDAYS` | INTEGER | NOT NULL |  |  |  |
| 21 | `DATECALCULATIONTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `QUALITYCONTROLDAYS` | INTEGER | NOT NULL |  |  |  |
| 23 | `BUYERCODE` | CHAR(50) |  | FK | foreign_key |  |
| 24 | `PURCHASEUOMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 25 | `PURCHASEBASEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `BARTYPECODE` | CHAR(2) |  | FK | foreign_key |  |
| 27 | `EXTERNALBARCODE` | VARCHAR(50) |  |  |  |  |
| 28 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 29 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 30 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 31 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 34 | `DATECALCULATIONTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 35 | `BUYERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 36 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `BLOCK` | SMALLINT | NOT NULL |  |  |  |
| 40 | `VALIDITYDATEFROM` | DATE |  |  |  |  |
| 41 | `QRCODE` | CHAR(200) |  |  |  |  |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BARCODETYPE_BARTYPE` | `BARTYPECODE` | [`BARCODETYPE`](../CORE_MASTER/BARCODETYPE.md) | `CODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.BARTYPECODE = BARCODETYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.COMPANYCODE = COMPANY.CODE` |
| `DATECALCULATIONTYPE_DATECALCULATIONTYPE` | `DATECALCULATIONTYPECOMPANYCODE`, `DATECALCULATIONTYPECODE` | [`DATECALCULATIONTYPE`](../OTHER/DATECALCULATIONTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.DATECALCULATIONTYPECOMPANYCODE = DATECALCULATIONTYPE.COMPANYCODE AND ORDERITEMORDERPARTNERLINK.DATECALCULATIONTYPECODE = DATECALCULATIONTYPE.CODE` |
| `INITIALS_BUYER` | `BUYERCOMPANYCODE`, `BUYERCODE` | [`INITIALS`](../CORE_MASTER/INITIALS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.BUYERCOMPANYCODE = INITIALS.COMPANYCODE AND ORDERITEMORDERPARTNERLINK.BUYERCODE = INITIALS.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND ORDERITEMORDERPARTNERLINK.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `ORDERPARTNER_ORDERPARTNER` | `COMPANYCODE`, `ORDERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND ORDERITEMORDERPARTNERLINK.ORDERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND ORDERITEMORDERPARTNERLINK.ORDPRNCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `UNITOFMEASURE_PURCHASEBASEUOM` | `PURCHASEBASEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `ORDERITEMORDERPARTNERLINK.PURCHASEBASEUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERITEMORDERPARTNERLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.ORDERITEMORDERPARTNERLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
