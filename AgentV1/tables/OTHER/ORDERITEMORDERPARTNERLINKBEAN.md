# DB2ADMIN.ORDERITEMORDERPARTNERLINKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 54
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 46931

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 3 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 4 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `EXTERNALITEMCODE` | CHAR(50) |  |  |  |  |
| 19 | `EXTERNALDRAWINGNUMBER` | CHAR(100) |  |  |  |  |
| 20 | `EXTERNALREFERENCE` | CHAR(30) |  |  |  |  |
| 21 | `LEADTIMEDAYS` | INTEGER | NOT NULL |  |  |  |
| 22 | `DATECALCULATIONTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `QUALITYCONTROLDAYS` | INTEGER | NOT NULL |  |  |  |
| 24 | `BUYERCODE` | CHAR(50) |  |  |  |  |
| 25 | `PURCHASEUOMTYPE` | CHAR(2) |  |  |  |  |
| 26 | `PURCHASEBASEUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 28 | `EXTERNALBARCODE` | VARCHAR(50) |  |  |  |  |
| 29 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 30 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 31 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 35 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 37 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 38 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 39 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 40 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 41 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 42 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 43 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 44 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 45 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 46 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 47 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 48 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 49 | `BLOCK` | SMALLINT | NOT NULL |  |  |  |
| 50 | `VALIDITYDATEFROM` | DATE |  |  |  |  |
| 51 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 52 | `QRCODE` | CHAR(200) |  |  |  |  |
| 53 | `QRBARCODE` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ORDERITEMORDERPARTNERLINKBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ORDITEMORDPARTNERLINKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.ORDERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.ORDERITEMORDERPARTNERLINKBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
