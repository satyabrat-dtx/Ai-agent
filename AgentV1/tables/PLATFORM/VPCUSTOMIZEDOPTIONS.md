# DB2ADMIN.VPCUSTOMIZEDOPTIONS

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 113944

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `VPADDRESS` | VARCHAR(250) |  |  |  |  |
| 2 | `OPENQUOTEBEFORERFQVALID` | SMALLINT | NOT NULL |  |  |  |
| 3 | `NOOFMONTHSOFMETRICS` | INTEGER | NOT NULL |  |  |  |
| 4 | `RFQMENU` | SMALLINT | NOT NULL |  |  |  |
| 5 | `UTILITYMENU` | SMALLINT | NOT NULL |  |  |  |
| 6 | `PROFILEMENU` | SMALLINT | NOT NULL |  |  |  |
| 7 | `CALENDARMENU` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CALCULATORMENU` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ACCOUNTMENU` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ASNMENU` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SENDMAILFORUSERCREATION` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SENDMAILFORRFQCREATION` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SENDMAILFORQUOTECREATION` | SMALLINT | NOT NULL |  |  |  |
| 14 | `SENDMAILFORPOCREATION` | SMALLINT | NOT NULL |  |  |  |
| 15 | `SENDMAILFORASNCREATION` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `SENDMAILFORPOREJECTION` | SMALLINT | NOT NULL |  |  |  |
| 22 | `OPEN` | CHAR(10) |  |  |  |  |
| 23 | `UNREAD` | CHAR(10) |  |  |  |  |
| 24 | `HEADERDISPLAYRFQPO` | CHAR(1) | NOT NULL |  |  |  |
| 25 | `OPENQUOTE` | CHAR(10) |  |  |  |  |
| 26 | `HEADERDISPLAYQUOTE` | CHAR(1) | NOT NULL |  |  |  |
| 27 | `QUOTEATTACHMENTFOLDER` | CHAR(10) |  |  |  |  |
| 28 | `SHAREDDRIVE` | SMALLINT | NOT NULL |  |  |  |
| 29 | `SHAREDDRIVEPATH` | VARCHAR(200) |  |  |  |  |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `FILEEXTENSIONSACCEPTED` | CLOB(1000000) |  |  |  |  |
| 33 | `NEWPWDLETTERTEMPLATECODE` | CHAR(30) |  | FK | foreign_key |  |
| 34 | `RESETPWDLETTERTEMPLATECODE` | CHAR(30) |  | FK | foreign_key |  |
| 35 | `RESETLINKDURATION` | INTEGER | NOT NULL |  |  |  |
| 36 | `USEPWPUSH` | SMALLINT | NOT NULL |  |  |  |
| 37 | `PASSWORDVALIDATIONPATTERN` | CHAR(160) |  |  |  |  |
| 38 | `PASSWORDPOLICY` | VARCHAR(960) |  |  |  |  |
| 39 | `FORCEPASSWORDCHANGE` | SMALLINT | NOT NULL |  |  |  |
| 40 | `DISABLEAFTERFAILEDLOGIN` | SMALLINT | NOT NULL |  |  |  |
| 41 | `NUMBEROFFAILEDLOGINS` | INTEGER | NOT NULL |  |  |  |
| 42 | `NOTIFICATIONEMAILUSERDISABLED` | CHAR(150) |  |  |  |  |
| 43 | `USERDISABLEDLETTERTEMPLATECODE` | CHAR(30) |  | FK | foreign_key |  |
| 44 | `NOTIFIYDISABLEDEXTERNALUSER` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLETTERTEMPLATE_NEWPWDLETTERTEMPLATE` | `COMPANYCODE`, `NEWPWDLETTERTEMPLATECODE` | [`ABSLETTERTEMPLATE`](../PLATFORM/ABSLETTERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `VPCUSTOMIZEDOPTIONS.COMPANYCODE = ABSLETTERTEMPLATE.COMPANYCODE AND VPCUSTOMIZEDOPTIONS.NEWPWDLETTERTEMPLATECODE = ABSLETTERTEMPLATE.CODE` |
| `ABSLETTERTEMPLATE_RESETPWDLETTERTEMPLATE` | `COMPANYCODE`, `RESETPWDLETTERTEMPLATECODE` | [`ABSLETTERTEMPLATE`](../PLATFORM/ABSLETTERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `VPCUSTOMIZEDOPTIONS.COMPANYCODE = ABSLETTERTEMPLATE.COMPANYCODE AND VPCUSTOMIZEDOPTIONS.RESETPWDLETTERTEMPLATECODE = ABSLETTERTEMPLATE.CODE` |
| `ABSLETTERTEMPLATE_USERDISABLEDLETTERTEMPLATE` | `COMPANYCODE`, `USERDISABLEDLETTERTEMPLATECODE` | [`ABSLETTERTEMPLATE`](../PLATFORM/ABSLETTERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `VPCUSTOMIZEDOPTIONS.COMPANYCODE = ABSLETTERTEMPLATE.COMPANYCODE AND VPCUSTOMIZEDOPTIONS.USERDISABLEDLETTERTEMPLATECODE = ABSLETTERTEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `VPCUSTOMIZEDOPTIONS_VPMADDATA` | [`VPMNOWADDITIONALDATA`](../OTHER/VPMNOWADDITIONALDATA.md) | `VPCUSTOMIZEDOPTIONSCOMPANYCODE` | `VPMNOWADDITIONALDATA.VPCUSTOMIZEDOPTIONSCOMPANYCODE = VPCUSTOMIZEDOPTIONS.COMPANYCODE` |

## Indexes

- `VPCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.VPADDRESS,
       t.OPENQUOTEBEFORERFQVALID,
       t.NOOFMONTHSOFMETRICS,
       t.RFQMENU,
       t.UTILITYMENU,
       t.PROFILEMENU,
       t.CALENDARMENU,
       t.CALCULATORMENU,
       t.ACCOUNTMENU,
       t.ASNMENU,
       t.SENDMAILFORUSERCREATION
FROM   DB2ADMIN.VPCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
