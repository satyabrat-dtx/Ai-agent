# DB2ADMIN.EXTOPLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 141
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235717

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 5 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 8 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `ORDERDATE` | DATE |  |  |  |  |
| 12 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 15 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 16 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 17 | `BOMVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 18 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 19 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 20 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 21 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 22 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 23 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 24 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 25 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 26 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 27 | `BOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 28 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 29 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 30 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 31 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 32 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 39 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 40 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 41 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 42 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `ENTRYITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 44 | `PROTOTYPEMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 45 | `ENTRYSUBCODE01` | CHAR(20) |  |  |  |  |
| 46 | `ENTRYSUBCODE02` | CHAR(10) |  |  |  |  |
| 47 | `ENTRYSUBCODE03` | CHAR(10) |  |  |  |  |
| 48 | `ENTRYSUBCODE04` | CHAR(10) |  |  |  |  |
| 49 | `ENTRYSUBCODE05` | CHAR(10) |  |  |  |  |
| 50 | `ENTRYSUBCODE06` | CHAR(10) |  |  |  |  |
| 51 | `ENTRYSUBCODE07` | CHAR(10) |  |  |  |  |
| 52 | `ENTRYSUBCODE08` | CHAR(10) |  |  |  |  |
| 53 | `ENTRYSUBCODE09` | CHAR(10) |  |  |  |  |
| 54 | `ENTRYSUBCODE10` | CHAR(10) |  |  |  |  |
| 55 | `ENTRYITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 56 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 57 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 58 | `PREVIOUSQUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 59 | `VIRTUALITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `VIRTUALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 62 | `SERVTRTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 63 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 64 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 65 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 66 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 67 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 68 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 69 | `ENTRYUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 70 | `ENTRYUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 71 | `ENTRYUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 72 | `ENTRYBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 73 | `ENTRYUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 74 | `CANCELLEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 75 | `USEDUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 76 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 77 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 78 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 79 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 80 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 81 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 82 | `EXTENDEDSTATUS` | CHAR(2) |  |  |  |  |
| 83 | `SUPPLIERWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 84 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 85 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 86 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 87 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 88 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 89 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 90 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 91 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 92 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 93 | `AREACODE` | CHAR(3) |  |  |  |  |
| 94 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 95 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 96 | `SUPPLIERACCEPTED` | SMALLINT | NOT NULL |  |  |  |
| 97 | `SUPPLIERACCEPTANCEDATE` | DATE |  |  |  |  |
| 98 | `PLANNEDPICKUPDATE` | DATE |  |  |  |  |
| 99 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 100 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 101 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 102 | `PREVIOUSPRICE` | DECIMAL(18,5) |  |  |  |  |
| 103 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 104 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 105 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 106 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 107 | `PREVIOUSFREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 108 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 109 | `PREVIOUSNETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 110 | `PREVIOUSTAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 111 | `PREVIOUSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 112 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 113 | `PREVIOUSUSEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 114 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 115 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 116 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 117 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 118 | `ORDPRNBANKORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 119 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 120 | `PREVIOUSCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 121 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 122 | `INITIALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 123 | `DELIVEREDDATE` | DATE |  |  |  |  |
| 124 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 125 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 126 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 127 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 128 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 129 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 130 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 131 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 132 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 133 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 134 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 135 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 136 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 137 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 138 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 139 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 140 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `EXTOPLINEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `EXTOPLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.LINETEMPLATECODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ORDERDATE
FROM   DB2ADMIN.EXTOPLINEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
