# DB2ADMIN.LCORDERDETAILPUR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 47
- **Primary key**: `COMPANYCODE`, `LCDETAILDIVISIONCODE`, `LCDETAILLCNO`, `LCDETAILLCDATE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222630

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `LCDETAILDIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `LCDETAILLCNO` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 4 | `LCDETAILLCDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `LCAMENDMENTNO` | CHAR(3) |  |  |  |  |
| 6 | `LCAMENDMENTDATE` | DATE |  |  |  |  |
| 7 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 8 | `PURCHASEORDERLINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `PURCHASEORDERLINECODE` | CHAR(15) |  |  |  |  |
| 10 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 11 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `STEP` | INTEGER | NOT NULL |  |  |  |
| 13 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 16 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `ARTICLEDESCRIPTION1` | VARCHAR(200) |  |  |  |  |
| 26 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 27 | `LCQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 28 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 30 | `RATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 31 | `GROSSAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 32 | `LASTDATEOFSHIPMENT` | DATE |  |  |  |  |
| 33 | `PRINTDESCRIPTION1` | VARCHAR(3000) |  |  |  |  |
| 34 | `PRINTDESCRIPTION2` | VARCHAR(200) |  |  |  |  |
| 35 | `PRINTDESCRIPTION3` | VARCHAR(200) |  |  |  |  |
| 36 | `PRINTDESCRIPTION4` | VARCHAR(200) |  |  |  |  |
| 37 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 38 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 39 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 40 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 41 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 42 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 43 | `TOLERANCEUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 44 | `TOLERANCEPLUS` | DECIMAL(15,5) |  |  |  |  |
| 45 | `TOLERANCEMINUS` | DECIMAL(15,5) |  |  |  |  |
| 46 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LCORDERDETAILPUR.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `LCORDERDETAILPUR.CURRENCYCODE = CURRENCY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LCORDERDETAILPUR.COMPANYCODE = DIVISION.COMPANYCODE AND LCORDERDETAILPUR.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LCORDERDETAILPUR.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND LCORDERDETAILPUR.ITEMTYPECODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_TOLERANCEUOM` | `TOLERANCEUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LCORDERDETAILPUR.TOLERANCEUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LCORDERDETAILPUR.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LCORDERDETAILPURUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LINENO,
       t.LCDETAILDIVISIONCODE,
       t.LCDETAILLCNO,
       t.LCDETAILLCDATE,
       t.LCAMENDMENTNO,
       t.LCAMENDMENTDATE,
       t.DIVISIONCODE,
       t.PURCHASEORDERLINECOUNTERCODE,
       t.PURCHASEORDERLINECODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE
FROM   DB2ADMIN.LCORDERDETAILPUR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
