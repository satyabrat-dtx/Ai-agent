# DB2ADMIN.ITEMSTLINKALLOWEDVALUEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 45
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 74645

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `LINKPOSITION` | INTEGER | NOT NULL |  |  |  |
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
| 18 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `CREATEFIKDONLY` | SMALLINT | NOT NULL |  |  |  |
| 20 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 21 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 22 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 23 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 24 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 25 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 27 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 28 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 29 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 30 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 31 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 32 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 33 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 34 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 35 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 36 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 37 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 38 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 39 | `OBSOLETE` | SMALLINT | NOT NULL |  |  |  |
| 40 | `PROTOTYPETEMPORARY` | SMALLINT | NOT NULL |  |  |  |
| 41 | `APPROVE` | SMALLINT | NOT NULL |  |  |  |
| 42 | `APPROVALTYPE` | INTEGER | NOT NULL |  |  |  |
| 43 | `REJECT` | SMALLINT | NOT NULL |  |  |  |
| 44 | `APPROVALSTATUS` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `ITEMSTLINKALLOWEDVALUEBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `ITEMSTLINKALLOWEDVALUEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.LINKPOSITION,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.ITEMSTLINKALLOWEDVALUEBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
