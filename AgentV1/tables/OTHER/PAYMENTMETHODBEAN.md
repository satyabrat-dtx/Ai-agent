# DB2ADMIN.PAYMENTMETHODBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 83
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147833

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `CODE` | CHAR(3) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `PAYMENTWITHBILLS` | SMALLINT | NOT NULL |  |  |  |
| 7 | `PAYMENTVARIANT` | CHAR(1) |  |  |  |  |
| 8 | `DISCOUNTDAYS1` | INTEGER | NOT NULL |  |  |  |
| 9 | `DISCOUNTRATE1` | DECIMAL(5,2) |  |  |  |  |
| 10 | `FIXEDDAY1` | INTEGER | NOT NULL |  |  |  |
| 11 | `MONTH1` | INTEGER | NOT NULL |  |  |  |
| 12 | `DISCOUNTDAYS2` | INTEGER | NOT NULL |  |  |  |
| 13 | `DISCOUNTRATE2` | DECIMAL(5,2) |  |  |  |  |
| 14 | `FIXEDDAY2` | INTEGER | NOT NULL |  |  |  |
| 15 | `MONTH2` | INTEGER | NOT NULL |  |  |  |
| 16 | `DISCOUNTDAYS3` | INTEGER | NOT NULL |  |  |  |
| 17 | `DISCOUNTRATE3` | DECIMAL(5,2) |  |  |  |  |
| 18 | `FIXEDDAY3` | INTEGER | NOT NULL |  |  |  |
| 19 | `MONTH3` | INTEGER | NOT NULL |  |  |  |
| 20 | `NETDAYS` | INTEGER | NOT NULL |  |  |  |
| 21 | `FIXEDDAYNET` | INTEGER | NOT NULL |  |  |  |
| 22 | `NETMONTH` | INTEGER | NOT NULL |  |  |  |
| 23 | `TOLERANCEDAYS` | INTEGER | NOT NULL |  |  |  |
| 24 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 25 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 26 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 27 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 28 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 29 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 33 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 34 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 35 | `FINLABELS` | CHAR(1) |  |  |  |  |
| 36 | `SPLITFIXDAY5` | INTEGER | NOT NULL |  |  |  |
| 37 | `SPLITDAYS1` | INTEGER | NOT NULL |  |  |  |
| 38 | `SPLITSHARE1` | INTEGER | NOT NULL |  |  |  |
| 39 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 40 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 41 | `INITIALDATE` | DATE |  |  |  |  |
| 42 | `FINALDATE` | DATE |  |  |  |  |
| 43 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 44 | `DUEDATEEXCEPTIONCODE` | CHAR(6) |  |  |  |  |
| 45 | `SPLITSTART` | CHAR(1) |  |  |  |  |
| 46 | `SPLITMONTHRULE` | CHAR(3) |  |  |  |  |
| 47 | `SPLITFIXDAY1` | INTEGER | NOT NULL |  |  |  |
| 48 | `SPLITFIXDAY2` | INTEGER | NOT NULL |  |  |  |
| 49 | `SPLITFIXDAY3` | INTEGER | NOT NULL |  |  |  |
| 50 | `SPLITFIXDAY4` | INTEGER | NOT NULL |  |  |  |
| 51 | `SPLITSHARECALC1` | DECIMAL(5,2) |  |  |  |  |
| 52 | `SPLITDAYS2` | INTEGER | NOT NULL |  |  |  |
| 53 | `SPLITSHARE2` | INTEGER | NOT NULL |  |  |  |
| 54 | `SPLITSHARECALC2` | DECIMAL(5,2) |  |  |  |  |
| 55 | `SPLITDAYS3` | INTEGER | NOT NULL |  |  |  |
| 56 | `SPLITSHARE3` | INTEGER | NOT NULL |  |  |  |
| 57 | `SPLITSHARECALC3` | DECIMAL(5,2) |  |  |  |  |
| 58 | `SPLITDAYS4` | INTEGER | NOT NULL |  |  |  |
| 59 | `SPLITSHARE4` | INTEGER | NOT NULL |  |  |  |
| 60 | `SPLITSHARECALC4` | DECIMAL(5,2) |  |  |  |  |
| 61 | `SPLITDAYS5` | INTEGER | NOT NULL |  |  |  |
| 62 | `SPLITSHARE5` | INTEGER | NOT NULL |  |  |  |
| 63 | `SPLITSHARECALC5` | DECIMAL(5,2) |  |  |  |  |
| 64 | `SPLITDAYS6` | INTEGER | NOT NULL |  |  |  |
| 65 | `SPLITSHARE6` | INTEGER | NOT NULL |  |  |  |
| 66 | `SPLITSHARECALC6` | DECIMAL(5,2) |  |  |  |  |
| 67 | `SPLITEXPIREDATERULE1` | CHAR(1) |  |  |  |  |
| 68 | `SPLITEXPIREDATERULE2` | CHAR(1) |  |  |  |  |
| 69 | `SPLITEXPIREDATERULE3` | CHAR(1) |  |  |  |  |
| 70 | `SPLITEXPIREDATERULE4` | CHAR(1) |  |  |  |  |
| 71 | `SPLITEXPIREDATERULE5` | CHAR(1) |  |  |  |  |
| 72 | `SPLITEXPIREDATERULE6` | CHAR(1) |  |  |  |  |
| 73 | `SPLITPAYMENTTYPE1CODE` | CHAR(3) |  |  |  |  |
| 74 | `SPLITPAYMENTTYPE2CODE` | CHAR(3) |  |  |  |  |
| 75 | `SPLITPAYMENTTYPE3CODE` | CHAR(3) |  |  |  |  |
| 76 | `SPLITPAYMENTTYPE4CODE` | CHAR(3) |  |  |  |  |
| 77 | `SPLITPAYMENTTYPE5CODE` | CHAR(3) |  |  |  |  |
| 78 | `SPLITPAYMENTTYPE6CODE` | CHAR(3) |  |  |  |  |
| 79 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 80 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 81 | `COLLECTIONMODE` | CHAR(1) |  |  |  |  |
| 82 | `EIPAYMENTTYPECODE` | CHAR(4) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PAYMENTMETHODBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.PAYMENTWITHBILLS,
       t.PAYMENTVARIANT,
       t.DISCOUNTDAYS1,
       t.DISCOUNTRATE1,
       t.FIXEDDAY1,
       t.MONTH1
FROM   DB2ADMIN.PAYMENTMETHODBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
